import requests
from data.test_url_data import TestUrlData
from data.test_auth_data import TestAuthData
import pytest


@pytest.fixture
def user_registration_and_delete():
    requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_COURIER}', data=TestAuthData.payload)
    yield
    response = requests.post(f"{TestUrlData.URL}{TestUrlData.PATH_LOGIN}", data=TestAuthData.payload)
    path = response.json()["id"]
    requests.delete(f'{TestUrlData.URL}{TestUrlData.PATH_COURIER}/{path}')
    requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_LOGIN}', data=TestAuthData.payload)
