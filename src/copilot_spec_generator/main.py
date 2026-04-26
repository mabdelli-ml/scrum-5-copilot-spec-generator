from __future__ import annotations

import uvicorn
from fastapi import FastAPI

from .generator import generate_spec
from .models import SpecRequest, SpecResponse

app = FastAPI(title="Copilot Spec Generator", version="0.1.0")


@app.get("/health")
def health() -> dict[str, bool]:
    return {"ok": True}


@app.post("/generate-spec", response_model=SpecResponse)
def generate(payload: SpecRequest) -> SpecResponse:
    return generate_spec(payload)


def run() -> None:
    uvicorn.run("copilot_spec_generator.main:app", host="0.0.0.0", port=8000, reload=False)
