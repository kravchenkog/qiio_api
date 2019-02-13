import random
import requests
import json


class Rest:

    def rest_get(self, app, route=None, url=None):
        if url == None:

            url = str(app.env.base_url) + str(route)
        else:
            url = url

        response = requests.request(
            "GET",
            url,
            headers=app.env.headers,
            params=app.env.params,
            cookies=app.env.cookies,
            verify=False)
        try:
            responce_j = json.loads(response.text)
            if type(responce_j) == list:
                responce_j = {'data': responce_j}

            responce_j['status_code'] = response.status_code

            return responce_j

        except:
            print(str(response))

    def rest_post(self, app, route, data):
        url = str(app.env.base_url) + str(route)
        if data is None:
            data = {}
        if app.env.headers:
            data = json.dumps(data)

        responce = requests.request(
            "POST",
            url,
            data=data,
            headers=app.env.headers,
            cookies=app.env.cookies,
            params=app.env.params)
        if responce.status_code != 200:
            print('STATUS CODE = {}  \n/ TEXT = {}  \n/ URL = {}  \n/ PARAMS = {}  \n/ DATA = {}'
                  .format(responce.status_code, responce.text, url, str(app.env.params), str(data)))
        elif responce.text == "":

            responce_j = {'data': responce.text, 'status_code': responce.status_code}
            return responce_j
        try:

            responce_j = json.loads(responce.text)
            responce_j['status_code'] = responce.status_code

            return responce_j
        except:
            print("_____________________________ERROR_JSON_LOADS_______________________________")
            print(responce.text)

            return responce

    def rest_put(self, app, route, data):
        url = str(app.env.base_url) + str(route)
        if data is None:
            data = {}
        if len(app.env.headers) > 1:
            data = json.dumps(data)

        responce = requests.request(
            "PUT",
            url,
            data=data,
            headers=app.env.headers,
            cookies=app.env.cookies,
            params=app.env.params)
        responce_j = {}
        try:

            responce_j['data'] = json.loads(responce.text)

        except:
            print("_____________________________ERROR_JSON_LOADS_______________________________")
            print(responce.text)

        responce_j['status_code'] = responce.status_code

        return responce_j

    def rest_delete(self, app, route, data=None):
        url = str(app.env.base_url) + str(route)
        if data is None:
            data = {}
        if len(app.env.headers) > 1:
            data = json.dumps(data)

        responce = requests.request(
            "DELETE",
            url,
            headers=app.env.headers,
            cookies=app.env.cookies,
            params=app.env.params)
        try:
            responce_j = {}
            if type(responce) == dict:
                responce_j = json.loads(responce.text)
            responce_j['status_code'] = responce.status_code

            return responce_j
        except:
            print("_____________________________ERROR_JSON_LOADS_______________________________")
            print(responce.text)
