import random
import requests
import json


class Rest:

    def rest_get(self, app, route=None, url=None):
        tr_data = self.get_transformed_data(app, route, data=None)
        if url:
            tr_data['url'] = url
        response = self.get_response_rest(app, tr_data, "GET")

        json_response = self.get_parsed_response_data(app, tr_data, response)
        return json_response

    def rest_post(self, app, route, data):
        tr_data = self.get_transformed_data(app, route, data)
        response = self.get_response_rest(app, tr_data, "POST")

        json_response = self.get_parsed_response_data(app, tr_data, response)

        return json_response

    def rest_put(self, app, route, data):
        tr_data = self.get_transformed_data(app, route, data)
        response = self.get_response_rest(app, tr_data, "PUT")

        json_response = self.get_parsed_response_data(app, tr_data, response)

        return json_response

    def rest_delete(self, app, route, data=None):
        tr_data = self.get_transformed_data(app, route, data)
        response = self.get_response_rest(app, tr_data, "DELETE")

        json_response = self.get_parsed_response_data(app, tr_data, response)

        return json_response

    def get_parsed_response_data(self, app, tr_data, response):
        if response.status_code != 200:
            self.print_resp_data(app, response, tr_data)

        if response.text == "":
            return {'data': response.text, 'status_code': response.status_code}

        try:
            responce_j = {'data': json.loads(response.text), 'status_code': response.status_code}

            return responce_j
        except:
            print("_____________________________ERROR_JSON_LOADS_______________________________")
            print(response.text)

    def print_resp_data(self, app, response, tr_data):
        print('STATUS CODE = {}  \n/ TEXT = {}  \n/ URL = {}  \n/ PARAMS = {}  \n/ DATA = {}'
              .format(response.status_code, response.text, tr_data['url'], str(app.env.params), str(tr_data['data'])))

    def get_transformed_data(self, app, route, data):
        url = str(app.env.base_url) + str(route)
        if data is None:
            data = {}
        if app.env.headers:
            data = json.dumps(data)
        return {'data': data, 'url': url}

    def get_response_rest(self, app, tr_data, resp_type):
        response = requests.request(method=resp_type, url=tr_data['url'], data=tr_data['data'], headers=app.env.headers,
                                    cookies=app.env.cookies, params=app.env.params, verify=False)
        return response
