"""Entrypoint for background worker tasks."""

from worker.tasks.process_incident import process_incident


def main() -> None:
    """Run the worker loop (placeholder)."""
    # In a real deployment, this might start Celery or another worker framework.
    print("Worker started. Ready to process incidents.")
    # Example invocation
    process_incident({"id": "example", "description": "Sample incident"})


if __name__ == "__main__":
    main()
