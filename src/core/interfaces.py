"""Core interfaces and contracts for AI Exploration 2026.

Shared across all modules. Changes require team consensus (Kalab, Bartek, Kamil).
Supports both Generative LLMs (System Two) and Decision Models (System One: Jev/Laya).
"""
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Literal, Optional, Union
from pydantic import BaseModel, Field


# --- System Two: Generative Models (LLMs) ---

class ModelRequest(BaseModel):
    """Standardized model request payload."""
    prompt: str
    system_prompt: Optional[str] = None
    temperature: float = 0.2
    max_tokens: int = 4096
    parameters: Dict[str, Any] = Field(default_factory=dict)


class ModelResponse(BaseModel):
    """Standardized model response with required course metadata."""
    content: str
    model_name: str
    model_version: str
    provider: str
    tier: str  # 'free' or 'paid'
    latency_seconds: float
    input_tokens: Optional[int] = None
    output_tokens: Optional[int] = None
    raw_response: Dict[str, Any] = Field(default_factory=dict)


class BaseModelProvider(ABC):
    """Abstract interface for all generative model providers (API and local)."""

    @abstractmethod
    def generate(self, request: ModelRequest) -> ModelResponse:
        """Execute a text generation call."""
        pass

    @abstractmethod
    def health_check(self) -> bool:
        """Verify provider availability."""
        pass


# --- System One: Decision Models (Jev / Laya / NanoJev) ---

class DecisionQuestion(BaseModel):
    """A typed question for a System One decision model."""
    id: str
    type: Literal["choice", "score", "noul"]  # choice=select from labels, score=scalar 2-10, noul=boolean prob
    question: str
    choices: Optional[List[str]] = None  # labels for 'choice' type


class DecisionRequest(BaseModel):
    """Payload for fast structured classification / routing / guardrails."""
    state: Dict[str, Any] = Field(default_factory=dict)
    questions: List[DecisionQuestion]
    context_text: Optional[str] = None


class DecisionResult(BaseModel):
    """Calibrated, typed answer to a single question."""
    question_id: str
    type: Literal["choice", "score", "noul"]
    value: Union[str, int, float, bool]
    confidence: float
    probabilities: Dict[str, float] = Field(default_factory=dict)


class DecisionResponse(BaseModel):
    """Response from decision model with sub-100ms latency tracking."""
    results: List[DecisionResult]
    model_name: str
    provider: str  # 'jev', 'laya', 'nanojev', etc.
    latency_ms: float
    raw_response: Dict[str, Any] = Field(default_factory=dict)


class BaseDecisionProvider(ABC):
    """Abstract interface for System One decision models."""

    @abstractmethod
    def decide(self, request: DecisionRequest) -> DecisionResponse:
        """Execute non-autoregressive decision pass."""
        pass
