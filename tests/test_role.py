import pytest
import random

class TestRole:
    @pytest.fixture(autouse=True)
    def remove_parameters(self, app):
        keys = list(app.env.params.keys())
        [app.env.params.pop(k, None) for k in keys if k != 'url']

    def test_WHEN_get_role_EXPECTED_response_code_200(self, app):
        # app.env.params['type'] = 'all'
        resp = app.rest.rest_get(app, route=app.route.get_roles)
        assert resp['status_code'] == 200

    def test_WHEN_post_new_role_EXPECTED_response_code_200(self, app, template):
        template_value = template
        random_role = random.choice([x for x in app.rest.rest_get(app, route=app.route.get_roles)['data']
                       if x['role'] == template_value])
        random_role['id'] = None
        random_role['template'] = template
        random_role['role'] = 'test_role' + app.string.get_random_string(10)
        random_role.pop('lastUpdated')
        random_role.pop('users')
        resp = app.rest.rest_post(app, app.route.new_role, random_role)
        assert resp['status_code'] == 200

    def test_WHEN_delete_new_role_EXPECTED_status_code_200(self, app):
        role_id = app.data_help.create_random_role_and_get_data(app)['data']['id']
        app.env.params['id'] = role_id

        resp = app.rest.rest_delete(app=app, route=app.route.del_role)
        assert resp['status_code'] == 200

    def test_WHEN_change_new_role_EXPECTED_status_code_200(self, app):
        new_role_data = app.data_help.create_random_role_and_get_data(app)['data']
        new_role_data['role'] = "test_role_" + app.string.get_random_string(10)

        resp = app.rest.rest_put(app, app.route.change_role, data=new_role_data)
        assert resp['status_code'] == 200
