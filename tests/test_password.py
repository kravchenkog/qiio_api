import pytest


class TestPassword:

    @pytest.fixture(autouse=True)
    def remove_parameters(self, app):
        app.data_help.remove_all_parameters_exsept_url(app)

    def test_WHEN_reset_password_EXPECTED_respomse_code_200(self, app):
        user = app.data_help.create_new_random_user_and_get_template_to_edit(app)['userdata']
        app.env.params['userId'] = user['id']
        resp = app.rest.rest_put(app, app.route.reset_password, data=None)
        assert resp['status_code'] == 200

    def test_WHEN_send_password_EXPECTED_status_code_200(self, app):
        user_data = app.data_help.create_new_random_user_and_get_template_to_edit(app)
        user = user_data['userdata']
        password = user_data['password']
        data = {
            "userEmail": user['email'],
            "userPassword": password,
            "login": user['login']
        }
        resp = app.rest.rest_post(app, app.route.send_password, data=data)
        assert resp['status_code'] == 200
