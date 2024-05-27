from tests.integrational_tests.api_client import client


class TestMisc:
    def test_healthcheck(self):
        res = client.get("/debug/healthcheck")
        assert res.status_code == 200
        assert res.json() == {"status": "OK"}
