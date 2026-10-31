
from fastapi.testclient import TestClient
from main import app, get_current_user
from models import User


# Temporary authenticated user for tests
test_user = User(
    id=1,
    email="test@example.com",
    password_hash="test-password-hash"
)


def override_get_current_user():
    return test_user


app.dependency_overrides[get_current_user] = override_get_current_user

client = TestClient(app)


def test_blank_prompt_is_rejected():
    response = client.post(
        "/ask",
        json={"prompt": "   ", "conversation_id": None}
    )
    assert response.status_code == 422


def test_empty_prompt_is_rejected():
    response = client.post(
        "/ask",
        json={"prompt": "", "conversation_id": None}
    )
    assert response.status_code == 422


def test_nonexistent_conversation_returns_404():
    response = client.get("/conversations/999999")
    assert response.status_code == 404


def test_deleting_nonexistent_conversation_returns_404():
    response = client.delete("/conversations/999999")
    assert response.status_code == 404


def test_authentication_is_required():
    app.dependency_overrides.pop(get_current_user)

    response = client.get("/conversations")
    assert response.status_code == 401

    app.dependency_overrides[get_current_user] = override_get_current_user
