from copilot_spec_generator.generator import generate_spec
from copilot_spec_generator.models import SpecRequest


def test_generate_spec_has_required_sections() -> None:
    req = SpecRequest(
        title="Checkout discount",
        brief="Allow users to apply discount codes during checkout.",
        request_type="feature",
        constraints=["No schema breaking changes"],
    )
    spec = generate_spec(req)

    assert spec.context
    assert len(spec.objectives) >= 1
    assert len(spec.scope) >= 1
    assert len(spec.requirements) >= 1
    assert len(spec.acceptance_criteria) >= 1
    assert len(spec.risks) >= 1
    assert len(spec.test_plan) >= 1
