import configuration
import requests
import data


def post_new_user(body):
        return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

data.kit_headers['Authorization'] = 'Bearer ' + response.json()['authToken']

print(data.kit_headers)

def get_new_user_token():
    response = post_new_user(data.user_body)
    return response.json()["authToken"]

def post_new_client_kit(kit_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=kit_body,
                         headers=data.kit_headers)

response = post_new_client_kit(data.kit_body)
print(response.status_code)
print (response.json())

