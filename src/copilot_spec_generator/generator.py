from __future__ import annotations

from .models import SpecRequest, SpecResponse


def _line_items(prefix: str, source: str, count: int) -> list[str]:
    return [f"{prefix} {i+1}: {source}" for i in range(count)]


def generate_spec(request: SpecRequest) -> SpecResponse:
    context = (
        f"Request type: {request.request_type}. "
        f"Problem statement: {request.brief.strip()}"
    )

    objectives = [
        f"Deliver a clear specification for: {request.title}",
        "Align product and engineering on expected behavior",
        "Reduce ambiguity before implementation",
    ]

    scope = [
        "Functional behavior",
        "Technical approach and API impacts",
        "Validation rules and edge cases",
    ]

    requirements = [
        f"Primary requirement: {request.brief.strip()}",
        "Provide output sections in a stable schema",
    ]
    requirements.extend([f"Constraint: {c}" for c in request.constraints])

    acceptance_criteria = _line_items(
        "AC",
        "Spec contains context, objectives, scope, requirements, risks, and tests",
        3,
    )

    risks = [
        "Input brief may be incomplete",
        "Generated text may require manual review",
        "Domain-specific constraints could be missing",
    ]

    test_plan = [
        "Unit test output structure and required sections",
        "Validate behavior with empty and rich constraints",
        "Manual review with a real product brief",
    ]

    return SpecResponse(
        context=context,
        objectives=objectives,
        scope=scope,
        requirements=requirements,
        acceptance_criteria=acceptance_criteria,
        risks=risks,
        test_plan=test_plan,
    )
