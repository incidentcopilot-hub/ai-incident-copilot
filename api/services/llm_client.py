class LLMClient:
    """Placeholder client for large language model interactions."""

    def __init__(self) -> None:
        self.model: str | None = None

    def summarize_incident(self, incident_text: str) -> str:
        """Summarize incident text using an LLM (not yet implemented)."""
        if not self.model:
            return "LLM model not configured"
        # Integration hook for LLM provider SDK would go here
        return incident_text
