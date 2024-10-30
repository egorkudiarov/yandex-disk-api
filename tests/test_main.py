import requests
import pytest

from tokens import Y as token
from main import create_folder

url = 'https://cloud-api.yandex.net/v1/disk/resources'
iurl = 'https://cloud-api.yandex.net/v1/dusk/resources'
path = 'new_folder'

@pytest.mark.parametrize(
    'url, path, token, expexted',
    ((url, path, token, 201),
     (url, None, token, 400),
     (url, path, None,  401),
     (iurl, path, token,404),
     (url, path, token, 409))
    )
def test_create_folder(url, path, token, expexted):
    response = create_folder(url, path, token)
    assert response.status_code == expexted