"""Core interfaces and contracts for AI Exploration 2026.

Shared across all modules. Changes require team consensus (Kalab, Bartek, Kamil).
"""
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


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
    """Abstract interface for all model providers (API and local)."""

    @abstractmethod
    def generate(self, request: ModelRequest) -> ModelResponse:
        """Execute a text generation call."""
        pass

    @abstractmethod
    def health_check(self) -> bool:
        """Verify provider availability."""
        pass
