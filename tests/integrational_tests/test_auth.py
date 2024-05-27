import pytest

from app.config import config
from tests.integrational_tests.api_client import client


@pytest.mark.parametrize(
    "headers, expected_status",
    [
        ({"Authorization": f"Bearer {config.API_TOKEN.get_secret_value()}"}, 200),
        ({"Authorization": "Bearer not_valid_token"}, 401),
        ({"Authorization": f"WrongScheme {config.API_TOKEN.get_secret_value()}"}, 403),
    ],
)
def test_bearer_auth(headers: dict, expected_status: int):
    req = client.get("/debug/auth", headers=headers)
    assert req.status_code == expected_status
    if expected_status == 200:
        assert req.json() == {"status": "OK"}
