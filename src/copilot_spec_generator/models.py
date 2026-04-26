from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field


class SpecRequest(BaseModel):
    title: str = Field(min_length=3)
    brief: str = Field(min_length=10)
    request_type: Literal["feature", "bugfix", "integration", "migration"] = "feature"
    constraints: list[str] = []


class SpecResponse(BaseModel):
    context: str
    objectives: list[str]
    scope: list[str]
    requirements: list[str]
    acceptance_criteria: list[str]
    risks: list[str]
    test_plan: list[str]
