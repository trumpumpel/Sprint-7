import requests
import pytest
import allure
import json
import random
import string

from data import lg, ps, fn
from helpers import login, password, first_name, login_pass


class TestLoginCourier:
    def test_courier_authorization(self):
        payload = {
            "login": lg,
            "password": ps
        }

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert response.status_code == 201
        assert response.text == '{"ok":true}'
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert response.status_code == 409
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert response.status_code == 200
        path = response.json()["id"]
        response_delete = requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{path}')
        assert response_delete.status_code == 200
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
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

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert response.status_code == 201
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/login', data=payload1)
        assert response.status_code == 404
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert response.status_code == 200
        path = response.json()["id"]
        response_delete = requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{path}')
        assert response_delete.status_code == 200
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
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

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert response.status_code == 201
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/login', data=payload1)
        assert response.status_code == 404
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert response.status_code == 200
        path = response.json()["id"]
        response_delete = requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{path}')
        assert response_delete.status_code == 200
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert response.status_code == 404

    def test_authorization_non_existent_user(self):
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/login', data=payload)
        assert response.status_code == 404

    def test_id_return(self):
        payload = {
            "login": lg,
            "password": ps
        }
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert response.status_code == 201
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert response.status_code == 200
        print(response.text)
        assert 'id' in response.text
        path = response.json()["id"]
        response_delete = requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{path}')
        assert response_delete.status_code == 200
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
        assert response.status_code == 404
