import random


class TestDevices:
    # comit
    def test_WHEN_get_devices_EXPECTED_status_code_is_200(self, app):
        resp = app.rest.rest_get(app, route=app.route.dev_list)
        assert resp['status_code'] == 200

    def test_WHEN_get_devices_EXPECTED_list_is_not_empty(self, app):
        resp = app.rest.rest_get(app, route=app.route.dev_list)
        assert len(resp['data']) > 0

    def test_WHEN_change_device_twin_EXPECTED_response_code_200(self, app):
        device = random.choice(app.rest.rest_get(app, route=app.route.dev_list)['data'])
        app.env.params['deviceId'] = device['deviceId']
        resp = app.rest.rest_put(app, app.route.change_dev_twin, data=device)

    def test_WHEN_get_device_events_EXPECTED_response_code_200(self, app):
        device = random.choice(app.rest.rest_get(app, route=app.route.dev_list)['data'])
        app.env.params['eventType'] = 'LastReport'
        app.env.params['deviceId'] = device['deviceId']
        resp = app.rest.rest_get(app, app.route.dev_events)
        assert resp['status_code'] == 200
