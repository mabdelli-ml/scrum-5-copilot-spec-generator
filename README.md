# SCRUM-5 Copilot Spec Generator

MVP project generated from Jira ticket `SCRUM-5`.

## Goal
Build a Copilot-style service that generates structured specifications from a product brief.

## Features (MVP)
- Generate functional + technical spec sections from a single input brief.
- Return a normalized schema ready for Markdown export.
- Keep output structure consistent for feature requests and bugfixes.

## Migration status
- `SCRUM-6`: migrated API layer from FastAPI to Flask.

## Run
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
copilot-spec-generator
```

Alternative with Flask CLI:
```bash
export FLASK_APP=copilot_spec_generator.main:app
flask run --host 0.0.0.0 --port 8000
```

## Example request
```bash
curl -X POST http://127.0.0.1:8000/generate-spec \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Add discount code flow",
    "brief": "Allow users to apply a discount code in checkout and show validation errors.",
    "request_type": "feature",
    "constraints": ["No breaking API changes", "Keep checkout under 2s p95"]
  }'
```

## Ticket traceability
- Jira: SCRUM-5
- Migration: SCRUM-6
- Source project: Software Team (SCRUM)

## Documentation
- Full architecture guide: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
- Documentation index: [docs/README.md](docs/README.md)
