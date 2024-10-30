import requests
from tokens import Y as token
url = 'https://cloud-api.yandex.net/v1/isk/resources'

def create_folder(url, path, token):
    params = {
        'path': path
    }
    headers = {
        'Authorization': f'OAuth {token}',
        }
    response = requests.put(url, params=params, headers=headers)
    return response
