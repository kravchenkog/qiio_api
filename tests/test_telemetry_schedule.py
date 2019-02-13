import pytest
import random
import time


class TestTelemetrySchedule():

    @pytest.fixture(autouse=True)
    def _remove_parameters(self, app):

        keys = list(app.env.params.keys())
        [app.env.params.pop(k, None) for k in keys if k != 'url']

    device_id = ''

    def test_WHEN_get_real_telemetry_EXPECTED_status_code_is_200(self, app, telemetry):
        device_id = random.choice(app.rest.rest_get(app, route=app.route.dev_list)['data'])
        app.env.params['deviceId'] = device_id['deviceId']
        app.env.params['type'] = telemetry

        resp = app.rest.rest_get(app, route=app.route.real_telemetry)
        assert resp['status_code'] == 200

    def test_WHEN_get_history_telemetry_EXPECTED_status_code_is_200(self, app, telemetry):
        dates = app.string.get_random_start_end_dates_unix()
        device = random.choice(app.rest.rest_get(app, route=app.route.dev_list)['data'])
        app.env.params['deviceId'] = device['deviceId']
        app.env.params['type'] = telemetry
        app.env.params['from'] = dates['start_date']
        app.env.params['to'] = time.time()
        app.env.params['addr'] = app.data_help.get_real_addr_from_one_device(device)

        resp = app.rest.rest_get(app, route=app.route.history_telemetry)
        assert resp['status_code'] == 200

    def test_WHEN_get_list_cellular_EXPECTED_response_code_400(self, app):
        app.env.params['page'] = random.randint(1, 50)
        app.env.params['number'] = random.randint(1, 50)
        resp = app.rest.rest_get(app, route=app.route.list_cell)
        assert resp['status_code'] == 400

    def test_WHEN_get_cellular_profile_EXPECTED_response_code_400(self, app):
        resp = app.rest.rest_get(app, route=app.route.list_cell_prof)
        assert resp['status_code'] == 400

    def test_WHEN_get_list_enrollments_EXPECTED_respose_code_400(self, app):
        app.env.params['page'] = random.randint(1, 50)
        app.env.params['number'] = random.randint(1, 50)

        resp = app.rest.rest_get(app, route=app.route.list_enroll)
        assert resp['status_code'] == 400

    def test_WHEN_post_schedule_EXPECTED_response_code_200(self, app, target):
        app.env.params['target'] = target
        device_list = app.rest.rest_get(app, route=app.route.dev_list)['data']
        data = {}

        if target != 'delta':
            for d in device_list:
                self.device_id = d['deviceId']
                app.env.params['deviceId'] = self.device_id
                firmware = app.rest.rest_get(app, route=app.route.list_firmware)
                if len(firmware['data']) > 0:
                    break

            if len(firmware['data']) == 0:
                print("TEST IS NOT COMPLETED \n firmware: " + str(firmware['data']))
                return

        if target in ['firmware', 'config', 'package']:

            app.env.params['deviceId'] = self.device_id
            app.env.params['method'] = "downloadFirmware"
            app.env.params['sourceUrl'] = random.choice(firmware['data'])
            data = {'payload': '{"packageUri":"{0}"}'}

        elif target == 'delta':

            app.env.params['method'] = "updateBeerstationText"
            app.env.params['deviceId'] = random.choice(device_list)['deviceId']
            if app.env.params['method'] == "updateBeerstationText":
                data = {'payload':
                            {"text_number": random.randint(1, 20),
                             "text": app.string.get_random_string(30)}}


        elif target == 'linux':
            app.env.params['method'] = 'swupdate'
            app.env.params['deviceId'] = random.choice(device_list)['deviceId']
            data = {'payload': {"packageUri": "{0}", 'type': random.randint(1, 3)}}
        app.env.params['time'] = int(app.string.get_random_start_end_dates_unix()['start_date'])
        resp = app.rest.rest_post(app, route=app.route.new_schedule, data=data)

        assert resp['status_code'] == 200
        print(str(resp))

    def test_WHEN_delete_schedule_EXPECTED_reponse_code_is_200(self, app):
        pass
        # TODO
