# AI Incident Copilot

Scaffold for an API and worker service that coordinates AI-assisted incident response. This project currently provides a basic FastAPI application with a health endpoint and placeholders for integrations.

## Structure

```
ai-incident-copilot/
├── api/
│   ├── main.py
│   ├── routes/
│   │   └── health.py
│   ├── services/
│   │   ├── datadog_client.py
│   │   ├── slack_client.py
│   │   └── llm_client.py
│   ├── models/
│   ├── schemas/
│   └── __init__.py
│
├── worker/
│   ├── worker.py
│   └── tasks/
│       └── process_incident.py
│
├── infra/
│   └── placeholder.md
│
├── tests/
│   └── test_health.py
│
├── scripts/
│   └── placeholder.md
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## Getting Started

1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the API locally:
   ```bash
   uvicorn api.main:app --reload
   ```
4. Run tests:
   ```bash
   pytest
   ```

## Docker

To build and run with Docker:
```bash
docker-compose up --build
```
