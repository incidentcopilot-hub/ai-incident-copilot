class SlackClient:
    """Placeholder client for Slack notifications."""

    def __init__(self) -> None:
        self.webhook_url: str | None = None

    def send_message(self, channel: str, message: str) -> None:
        """Send a message to Slack (not yet implemented)."""
        if self.webhook_url:
            # Integration hook for Slack SDK would go here
            pass
