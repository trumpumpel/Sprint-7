import requests
from data import URL, payload, PATH_COURIER, PATH_LOGIN
import pytest


@pytest.fixture
def user_registration_and_delete():
    requests.post(f'{URL}{PATH_COURIER}', data=payload)
    yield
    response = requests.post(f"{URL}{PATH_LOGIN}", data=payload)
    path = response.json()["id"]
    requests.delete(f'{URL}{PATH_COURIER}/{path}')
    requests.post(f'{URL}{PATH_LOGIN}', data=payload)


@pytest.fixture
def user_delete():
    response = requests.post(f"{URL}{PATH_LOGIN}", data=payload)
    path = response.json()["id"]
    requests.delete(f'{URL}{PATH_COURIER}/{path}')
    requests.post(f'{URL}{PATH_LOGIN}', data=payload)
