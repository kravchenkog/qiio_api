import pytest


class TestInitials:
    @pytest.fixture(autouse=True)
    def _remove_parameters(self, app):
        keys = list(app.env.params.keys())
        [app.env.params.pop(k, None) for k in keys if k != 'url']

    def test_WHEN_get_initials_EXPECTED_response_code_200(self, app):
        resp = app.rest.rest_get(app, route=app.route.list_init)
        assert resp['status_code'] == 200
