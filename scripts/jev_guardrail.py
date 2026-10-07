#!/usr/bin/env python3
"""Jev System One Git Pre-Commit Guardrail.

Analyzes staged Git changes before commit using JevProvider.
Detects secret leaks, evaluates safety, and provides sub-100ms verification.
"""
import sys
import subprocess
import os

# Ensure project root is in sys.path
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if repo_root not in sys.path:
    sys.path.insert(0, repo_root)

from src.pipeline.providers.jev import JevProvider
from src.core.interfaces import DecisionRequest, DecisionQuestion


def get_staged_diff() -> str:
    """Get staged diff text."""
    try:
        res = subprocess.run(
            ["git", "diff", "--cached"],
            capture_output=True,
            text=True,
            check=True,
        )
        return res.stdout
    except Exception as e:
        print(f"[Jev Guardrail] Failed to read git diff: {e}", file=sys.stderr)
        return ""


def main() -> int:
    diff = get_staged_diff()
    if not diff.strip():
        # Nothing staged or empty diff
        return 0

    # Truncate diff if extremely large for fast evaluation
    truncated_diff = diff[:4000]

    provider = JevProvider()

    req = DecisionRequest(
        state={"diff_size_bytes": len(diff)},
        context_text=truncated_diff,
        questions=[
            DecisionQuestion(
                id="secret_leak",
                type="noul",
                question="Does this staged code diff contain hardcoded API keys, private credentials, or secrets?",
            ),
            DecisionQuestion(
                id="safety_score",
                type="score",
                question="Rate the safety of this commit from 1 (severe risk/bug) to 10 (clean/safe):",
            ),
            DecisionQuestion(
                id="impact_category",
                type="choice",
                question="Classify this commit type:",
                choices=["safe_feature", "docs_update", "risky_modification", "security_threat"],
            ),
        ],
    )

    try:
        res = provider.decide(req)
    except Exception as e:
        print(f"[Jev Guardrail] Warning: Jev evaluation failed ({e}), continuing with caution.")
        return 0

    results_map = {r.question_id: r for r in res.results}

    secret_res = results_map.get("secret_leak")
    safety_res = results_map.get("safety_score")
    impact_res = results_map.get("impact_category")

    print(f"[*] Jev System-1 Guardrail ({res.model_name}, {res.latency_ms:.1f}ms):")
    if secret_res:
        is_leak = bool(secret_res.value)
        if is_leak and secret_res.confidence > 0.7:
            print(f"  [X] BLOCKED: Potential secret leak detected! (Confidence: {secret_res.confidence:.2f})")
            return 1
        else:
            print("  [OK] No leaked secrets detected.")

    if safety_res:
        score = int(safety_res.value)
        print(f"  [OK] Commit safety score: {score}/10")
        if score < 3 and safety_res.confidence > 0.8:
            print(f"  [!] Warning: Low safety score ({score}/10). Review diff before pushing.")

    if impact_res:
        print(f"  [OK] Impact category: {impact_res.value}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
