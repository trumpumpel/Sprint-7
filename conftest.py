import requests
from data import url, lg, ps, fn
import allure
import random
import string
import pytest

data = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [
                "BLACK"
            ]

        }
payload = {
    "login": lg,
    "password": ps,
    "firstName": fn
}

payload4 = {
    "login": lg,
    "password": ps
}


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


login = generate_random_string(10)
password = generate_random_string(10)
first_name = generate_random_string(10)


@pytest.fixture
def user_registration_and_delete():
    requests.post(f'{url}/api/v1/courier', data=payload)
    yield
    response = requests.post(f"{url}/api/v1/courier/login", data=payload)
    path = response.json()["id"]
    requests.delete(f'{url}/api/v1/courier/{path}')
    requests.post(f'{url}/api/v1/courier/login', data=payload)


@pytest.fixture
def user_registration():
    requests.post(f'{url}/api/v1/courier', data=payload)
