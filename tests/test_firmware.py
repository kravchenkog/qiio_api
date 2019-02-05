import pytest


class TestFirmware:
    @pytest.fixture(autouse=True)
    def _remove_parameters(self, app):
        keys = list(app.env.params.keys())
        [app.env.params.pop(k, None) for k in keys if k != 'url']

    def test_WHEN_get_firmware_EXPECTED_response_code_is_200(self, app, target):
        app.env.params['target'] = target
        resp = app.rest.rest_get(app, route=app.route.list_firmware)
        assert resp['status_code'] == 200
