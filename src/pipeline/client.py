"""Pipeline client dispatcher for invoking models."""
from typing import Dict
from src.core.interfaces import BaseModelProvider, ModelRequest, ModelResponse


class PipelineClient:
    """Dispatches requests to registered model providers."""

    def __init__(self) -> None:
        self.providers: Dict[str, BaseModelProvider] = {}

    def register(self, name: str, provider: BaseModelProvider) -> None:
        self.providers[name] = provider

    def execute(self, provider_name: str, request: ModelRequest) -> ModelResponse:
        if provider_name not in self.providers:
            raise ValueError(f"Provider '{provider_name}' not registered.")
        return self.providers[provider_name].generate(request)
