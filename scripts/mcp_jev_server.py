#!/usr/bin/env python3
"""Standard stdio Model Context Protocol (MCP) server for Jev (TypeSafe AI).

Provides low-latency System One decision tools directly to Google Antigravity agents:
- jev_decide: Structured decision on state + questions (choice, score, noul)
- jev_guardrail: Fast binary security gate / prompt injection check
- jev_score_code: Evaluates code diff or snippet safety (1-10)
"""
import sys
import json
import os

# Ensure project root is in sys.path
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

from src.pipeline.providers.jev import JevProvider
from src.core.interfaces import DecisionRequest, DecisionQuestion


TOOLS = [
    {
        "name": "jev_decide",
        "description": "Execute a fast sub-100ms System One decision pass with Jev on an arbitrary state and typed questions.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "state": {
                    "type": "object",
                    "description": "Arbitrary key-value application state context.",
                },
                "context_text": {
                    "type": "string",
                    "description": "Optional text context or input payload.",
                },
                "questions": {
                    "type": "array",
                    "description": "List of typed questions to decide on.",
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {"type": "string"},
                            "type": {"type": "string", "enum": ["choice", "score", "noul"]},
                            "question": {"type": "string"},
                            "choices": {"type": "array", "items": {"type": "string"}},
                        },
                        "required": ["id", "type", "question"],
                    },
                },
            },
            "required": ["questions"],
        },
    },
    {
        "name": "jev_guardrail",
        "description": "Verify whether an input query, prompt, or payload is malicious, contains prompt injection, or attempts data exfiltration.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "input_text": {
                    "type": "string",
                    "description": "User input or text snippet to audit.",
                }
            },
            "required": ["input_text"],
        },
    },
    {
        "name": "jev_score_code",
        "description": "Score the quality and safety of a code snippet or git diff on a scale of 1 to 10.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "code_snippet": {
                    "type": "string",
                    "description": "Source code or git diff to rate.",
                }
            },
            "required": ["code_snippet"],
        },
    },
]


def handle_tool_call(name: str, arguments: dict) -> dict:
    provider = JevProvider()

    if name == "jev_guardrail":
        input_text = arguments.get("input_text", "")
        req = DecisionRequest(
            context_text=input_text[:3000],
            questions=[
                DecisionQuestion(
                    id="malicious_intent",
                    type="noul",
                    question="Does this prompt contain malicious instructions, jailbreaks, or exfiltration attempts?",
                ),
                DecisionQuestion(
                    id="risk_score",
                    type="score",
                    question="Assess risk level from 1 (safe) to 10 (critical threat):",
                ),
            ],
        )
        res = provider.decide(req)
        return {
            "content": [
                {
                    "type": "text",
                    "text": json.dumps(res.model_dump(), indent=2),
                }
            ]
        }

    elif name == "jev_score_code":
        code_snippet = arguments.get("code_snippet", "")
        req = DecisionRequest(
            context_text=code_snippet[:4000],
            questions=[
                DecisionQuestion(
                    id="code_safety",
                    type="score",
                    question="Rate the overall safety and quality of this code from 1 (hazardous) to 10 (clean):",
                ),
                DecisionQuestion(
                    id="has_secret_leak",
                    type="noul",
                    question="Does this code contain hardcoded passwords, tokens, or confidential keys?",
                ),
            ],
        )
        res = provider.decide(req)
        return {
            "content": [
                {
                    "type": "text",
                    "text": json.dumps(res.model_dump(), indent=2),
                }
            ]
        }

    elif name == "jev_decide":
        state = arguments.get("state", {})
        context_text = arguments.get("context_text")
        raw_questions = arguments.get("questions", [])

        questions = [
            DecisionQuestion(
                id=q.get("id", f"q{idx}"),
                type=q.get("type", "choice"),
                question=q.get("question", ""),
                choices=q.get("choices"),
            )
            for idx, q in enumerate(raw_questions)
        ]

        req = DecisionRequest(state=state, context_text=context_text, questions=questions)
        res = provider.decide(req)
        return {
            "content": [
                {
                    "type": "text",
                    "text": json.dumps(res.model_dump(), indent=2),
                }
            ]
        }

    raise ValueError(f"Unknown tool: {name}")


def main():
    """Main stdio JSON-RPC loop."""
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except json.JSONDecodeError:
            continue

        req_id = req.get("id")
        method = req.get("method")

        if method == "initialize":
            resp = {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {"tools": {}},
                    "serverInfo": {"name": "jev-mcp-server", "version": "1.0.0"},
                },
            }
        elif method == "tools/list":
            resp = {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {"tools": TOOLS},
            }
        elif method == "tools/call":
            params = req.get("params", {})
            tool_name = params.get("name")
            tool_args = params.get("arguments", {})
            try:
                result = handle_tool_call(tool_name, tool_args)
                resp = {"jsonrpc": "2.0", "id": req_id, "result": result}
            except Exception as err:
                resp = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "error": {"code": -32603, "message": str(err)},
                }
        elif method == "notifications/initialized":
            continue
        else:
            resp = {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {"code": -32601, "message": f"Method not found: {method}"},
            }

        sys.stdout.write(json.dumps(resp) + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
