import pytest
from fastapi.testclient import TestClient

from app.config import config
from app.main import app

client = TestClient(app)


@pytest.mark.parametrize(
    "headers, expected_status",
    [
        ({"Authorization": f"Bearer {config.API_TOKEN}"}, 200),
        ({"Authorization": "Bearer not_valid_token"}, 401),
        ({"Authorization": f"WrongScheme {config.API_TOKEN}"}, 403),
    ],
)
def test_bearer_auth(headers: dict, expected_status: int):
    req = client.get("/debug/auth", headers=headers)
    assert req.status_code == expected_status
