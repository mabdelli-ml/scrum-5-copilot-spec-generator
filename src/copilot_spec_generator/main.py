from __future__ import annotations

from flask import Flask, jsonify, request
from pydantic import ValidationError

from .generator import generate_spec
from .models import SpecRequest

app = Flask("copilot-spec-generator")


@app.get("/health")
def health() -> tuple[dict[str, bool], int]:
    return {"ok": True}, 200


@app.post("/generate-spec")
def generate() -> tuple[dict, int]:
    raw_payload = request.get_json(silent=False)
    try:
        payload = SpecRequest.model_validate(raw_payload)
    except ValidationError as exc:
        return jsonify({"error": "validation_error", "details": exc.errors()}), 400

    spec = generate_spec(payload)
    return jsonify(spec.model_dump()), 200


def run() -> None:
    app.run(host="0.0.0.0", port=8000)
