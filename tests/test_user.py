import random
import pytest




class TestUser:
    @pytest.fixture(autouse=True)
    def remove_parameters(self, app):
        keys = list(app.env.params.keys())
        [app.env.params.pop(k, None) for k in keys if k != 'url']

    def test_WHEN_get_user_EXPECTED_status_code_200(self, app):
        resp = app.rest.rest_get(app, route=app.route.user)
        assert resp['status_code'] == 200

    def test_WHEN_get_list_users_EXPECTED_status_code_200(self, app):
        app.env.params['number'] = random.randint(0, 100)
        resp = app.rest.rest_get(app, route=app.route.list_users)
        assert resp['status_code'] == 200

    def test_WHEN_new_user_AND_data_is_proper_EXPECTED_response_code_200(self, app):
        device_id = random.choice(app.rest.rest_get(app, route=app.route.dev_list)['data'])['deviceId']
        data = app.data_help.get_random_user_data(app, device_id)
        app.env.params['domain'] = 'goms-test.qiio.cloud'
        app.env.params['password'] = 'JfR^cym&S$'

        resp = app.rest.rest_post(app=app, data=data, route=app.route.new_user)
        resp['status_code'] = 200

    def test_WHEN_delete_user_EXPECTED_response_code_is_200(self, app):
        # CREATE USER
        device_id = random.choice(app.rest.rest_get(app, route=app.route.dev_list)['data'])['deviceId']
        data = app.data_help.get_random_user_data(app, device_id)
        app.env.params['domain'] = 'goms-test.qiio.cloud'
        app.env.params['password'] = 'JfR^cym&S$'
        resp = app.rest.rest_post(app=app, data=data, route=app.route.new_user)

        # GET_CREATED_USER
        app.data_help.remove_parameters(app)
        user_id = [x['id'] for x in app.rest.rest_get(app, route=app.route.list_users)['result'] if
                   x['email'] == data['email']]

        # DELETE USER
        app.env.params['userId'] = user_id
        resp = app.rest.rest_delete(app=app, route=app.route.del_user)
        assert resp['status_code'] == 200

    def test_WHEN_put_change_user_AND_data_proper_EXPECTED_response_code_200(self, app):
        user = app.data_help.create_new_random_user_and_get_template_to_edit(app)
        new_first_name = app.string.get_random_string(10)
        new_user_data = user['userdata']
        new_user_data['firstName'] = new_first_name

        resp = app.rest.rest_put(app, route=app.route.change_user, data=new_user_data)
        assert resp['status_code'] == 200

