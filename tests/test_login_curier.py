import requests
import pytest
import allure
import json
import random
import string

from data import lg, ps, fn, URL, URL_LOG
from helpers import login, password, first_name, login_pass


class TestLoginCourier:
    def test_courier_authorization(self):
        payload = {
            "login": lg,
            "password": ps
        }

        response = requests.post(URL, data=payload)
        assert response.status_code == 201
        assert response.text == '{"ok":true}'
        response = requests.post(URL, data=payload)
        assert response.status_code == 409
        response = requests.post(f'{URL}/login', data=payload)
        assert response.status_code == 200
        path = response.json()["id"]
        response_delete = requests.delete(f'{URL}/{path}')
        assert response_delete.status_code == 200
        response = requests.post(f'{URL}/login', data=payload)
        assert response.status_code == 404

    def test_courier_authorization_empty_field_login(self):
        payload = {
            "login": lg,
            "password": ps
        }
        payload1 = {
            "login": '',
            "password": ps
        }

        response = requests.post(URL, data=payload)
        assert response.status_code == 201
        response = requests.post(URL_LOG, data=payload1)
        assert response.status_code == 404
        response = requests.post(f'{URL}/login', data=payload)
        assert response.status_code == 200
        path = response.json()["id"]
        response_delete = requests.delete(f'{URL}/{path}')
        assert response_delete.status_code == 200
        response = requests.post(f'{URL}/login', data=payload)
        assert response.status_code == 404

    def test_courier_authorization_empty_field_password(self):
        payload = {
            "login": lg,
            "password": ps
        }

        payload1 = {
            "login": lg,
            "password": ''
        }

        response = requests.post(URL, data=payload)
        assert response.status_code == 201
        response = requests.post(URL_LOG, data=payload1)
        assert response.status_code == 404
        response = requests.post(f'{URL}/login', data=payload)
        assert response.status_code == 200
        path = response.json()["id"]
        response_delete = requests.delete(f'{URL}/{path}')
        assert response_delete.status_code == 200
        response = requests.post(f'{URL}/login', data=payload)
        assert response.status_code == 404

    def test_authorization_non_existent_user(self):
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(URL_LOG, data=payload)
        assert response.status_code == 404

    def test_id_return(self):
        payload = {
            "login": lg,
            "password": ps
        }
        response = requests.post(URL, data=payload)
        assert response.status_code == 201
        response = requests.post(f'{URL}/login', data=payload)
        assert response.status_code == 200
        print(response.text)
        assert 'id' in response.text
        path = response.json()["id"]
        response_delete = requests.delete(f'{URL}/{path}')
        assert response_delete.status_code == 200
        response = requests.post(f'{URL}/login', data=payload)
        assert response.status_code == 404
