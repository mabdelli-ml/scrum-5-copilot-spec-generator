from copilot_spec_generator.main import app


def test_health_endpoint() -> None:
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"ok": True}


def test_generate_spec_endpoint() -> None:
    client = app.test_client()
    response = client.post(
        "/generate-spec",
        json={
            "title": "Checkout discount",
            "brief": "Allow users to apply discount codes during checkout.",
            "request_type": "feature",
            "constraints": ["No schema breaking changes"],
        },
    )

    data = response.get_json()
    assert response.status_code == 200
    assert data["context"]
    assert len(data["acceptance_criteria"]) >= 1
