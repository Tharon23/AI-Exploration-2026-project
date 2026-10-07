"""Jev (TypeSafe AI) System One decision model provider.

Implements non-autoregressive, calibrated decisions (choice, score, noul).
API reference: https://github.com/codaaiteam/jev-ai, https://github.com/v-modal/awesome-jev-tools
"""
import time
import os
import json
import urllib.request
import urllib.error
from typing import Any, Dict, List, Optional
from src.core.interfaces import (
    BaseDecisionProvider,
    DecisionRequest,
    DecisionResponse,
    DecisionResult,
)


class JevProvider(BaseDecisionProvider):
    """Client for TypeSafe AI Jev decision API (POST /v1/systemone)."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = "https://api.typesafe.ai/v1",
        timeout_seconds: float = 3.0,
    ) -> None:
        self.api_key = api_key or os.getenv("TYPESAFE_API_KEY", "")
        self.base_url = os.getenv("JEV_BASE_URL", base_url).rstrip("/")
        self.timeout = timeout_seconds

    def decide(self, request: DecisionRequest) -> DecisionResponse:
        """Execute a sub-300ms decision call against Jev API."""
        start_time = time.perf_counter()

        # If no API key configured or local mock requested, fallback to local deterministic evaluator
        if not self.api_key:
            return self._mock_fallback(request, start_time)

        endpoint = f"{self.base_url}/systemone"
        payload = {
            "state": request.state,
            "context": request.context_text,
            "questions": [
                {
                    "id": q.id,
                    "type": q.type,
                    "question": q.question,
                    "choices": q.choices,
                }
                for q in request.questions
            ],
        }

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
            "User-Agent": "AI-Exploration-2026/1.0",
        }

        req = urllib.request.Request(
            endpoint,
            data=json.dumps(payload).encode("utf-8"),
            headers=headers,
            method="POST",
        )

        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                latency_ms = (time.perf_counter() - start_time) * 1000

                results: List[DecisionResult] = []
                for item in data.get("results", []):
                    results.append(
                        DecisionResult(
                            question_id=item["id"],
                            type=item["type"],
                            value=item["value"],
                            confidence=item.get("confidence", 1.0),
                            probabilities=item.get("probabilities", {}),
                        )
                    )

                return DecisionResponse(
                    results=results,
                    model_name="jev-v1",
                    provider="typesafe",
                    latency_ms=latency_ms,
                    raw_response=data,
                )
        except Exception as e:
            # Fallback to local rule evaluator if API call fails
            return self._mock_fallback(request, start_time, error=str(e))

    def _mock_fallback(
        self, request: DecisionRequest, start_time: float, error: Optional[str] = None
    ) -> DecisionResponse:
        """Deterministic local fallback when API key is missing or offline."""
        latency_ms = (time.perf_counter() - start_time) * 1000
        results: List[DecisionResult] = []

        for q in request.questions:
            if q.type == "noul":
                results.append(
                    DecisionResult(
                        question_id=q.id,
                        type="noul",
                        value=False,
                        confidence=0.95,
                        probabilities={"true": 0.05, "false": 0.95},
                    )
                )
            elif q.type == "score":
                results.append(
                    DecisionResult(
                        question_id=q.id,
                        type="score",
                        value=5,
                        confidence=0.90,
                        probabilities={"score_5": 0.90},
                    )
                )
            elif q.type == "choice" and q.choices:
                results.append(
                    DecisionResult(
                        question_id=q.id,
                        type="choice",
                        value=q.choices[0],
                        confidence=0.88,
                        probabilities={q.choices[0]: 0.88},
                    )
                )

        return DecisionResponse(
            results=results,
            model_name="jev-local-fallback",
            provider="local",
            latency_ms=latency_ms,
            raw_response={"notice": "Executed via local fallback", "error": error},
        )
