"""Evaluation scorer module for assessing model outputs."""
from typing import Any, Dict, List


class BenchmarkScorer:
    """Calculates accuracy, consistency, and variance metrics."""

    @staticmethod
    def calculate_metrics(runs: List[Dict[str, Any]]) -> Dict[str, float]:
        """Aggregate metrics over multiple runs of the same prompt."""
        if not runs:
            return {"runs_count": 0}
        return {
            "runs_count": len(runs),
            "avg_latency": sum(r.get("latency_seconds", 0) for r in runs) / len(runs),
        }
