class DatadogClient:
    """Placeholder client for Datadog interactions."""

    def __init__(self) -> None:
        self.enabled = False

    def send_metric(self, name: str, value: float) -> None:
        """Send a metric to Datadog (not yet implemented)."""
        if self.enabled:
            # Integration hook for Datadog SDK would go here
            pass
