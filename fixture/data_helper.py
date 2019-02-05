import random


class DataHelper:

    def get_real_addr_from_one_device(self, device):
        li = []
        for x in device['properties']['desired']:
            if 'node' in x:
                li.append(x)

        li2 = []
        for x in range(len(li)):
            li2.append(device['properties']['desired'][li[x]]['addr'])

        li3 = self.get_is_not_digit_values_from_list(li2)
        return li3

    def get_is_not_digit_values_from_list(self, li):
        part1 = [x for x in li if x.isdigit() == False]
        part2 = [x for x in li if x.isdigit() == True and int(x)]
        if len(part2):
            part1.extend(part2)
            return part1
        else:
            return part1

    def get_random_user_data(self, app, device_list):

        data = {
            'login': 'test_user_' + app.string.get_random_string(10),
            'firstName': 'test_name' + app.string.get_random_string(5),
            'lastName': 'test_lastName' + app.string.get_random_string(5),
            'email': 'test_email' + app.string.get_random_email(),
            'devices': [{
                'deviceId': device_list,
                'access': 'full'
            }],
            "company": app.env.params['url'],
            "Permissions": [{
                "role": "User",
                "companies": [
                    app.env.params['url']
                ]},
            ],
            'reports': [],
            'type': 'Users'

        }
        return data

    def remove_parameters(self, app):
        keys = list(app.env.params.keys())
        [app.env.params.pop(k, None) for k in keys if k != 'url']

    def create_new_random_user_and_get_template_to_edit(self, app):

        password = 'JfR^cym&S$'
        self.remove_parameters(app)
        device_id = random.choice(app.rest.rest_get(app, route=app.route.dev_list)['data'])['deviceId']
        user_data = self.get_random_user_data(app, device_id)
        app.env.params['domain'] = app.env.params['url']
        app.env.params['password'] = password
        resp = app.rest.rest_post(app=app, data=user_data, route=app.route.new_user)

        self.remove_parameters(app)
        user = [x for x in app.rest.rest_get(app, route=app.route.list_users)['result'] if
                x['email'] == user_data['email']][0]

        return {'userdata': user, "password": password}

    def create_random_role_and_get_data(self, app):
        random_role = random.choice([x for x in app.rest.rest_get(app, route=app.route.get_roles)['data']
                                     if x['role'] == 'User'])
        random_role.pop('id')
        random_role['role'] = 'test_role' + app.string.get_random_string(10)
        random_role['template'] = 'User'
        random_role.pop('users')
        resp = app.rest.rest_post(app, app.route.new_role, random_role)
        resp.pop('status_code')

        return resp

    def remove_all_parameters_exsept_url(self, app):
        keys = list(app.env.params.keys())
        [app.env.params.pop(k, None) for k in keys if k != 'url']

    def clean_test_roles(self, app):
        roles = app.rest.rest_get(app, route=app.route.get_roles)
        for ro in roles['data']:
            if 'test_role' in ro['role']:
                app.env.params['id'] = ro['id']
                app.rest.rest_delete(app=app, route=app.route.del_role)
                self.remove_all_parameters_exsept_url(app)


    def clean_test_users(self, app):
        users = app.rest.rest_get(app, route=app.route.list_users)
        for us in users['result']:
            if 'test_user' in us['login']:
                app.env.params['userId'] = us['id']
                app.rest.rest_delete(app=app, route=app.route.del_user)
                self.remove_all_parameters_exsept_url(app)
