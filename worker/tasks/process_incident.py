"""Task definitions for incident processing."""


def process_incident(incident: dict) -> None:
    """Process an incident payload (placeholder)."""
    incident_id = incident.get("id", "unknown")
    print(f"Processing incident {incident_id}")
