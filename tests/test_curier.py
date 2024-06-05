import allure
import requests

from data import lg, ps, fn, URL
from helpers import password, first_name


class TestCourier:

    @allure.title('Проверка алгоритмов создания курьера')
    @allure.step('Проверка создания курьера и двух с одинаковыми данными')
    def test_register_two_couriers(self):
        payload = {
            "login": lg,
            "password": ps,
            "firstName": fn
        }
        response = requests.post(f'{URL}/api/v1/courier', data=payload)
        assert response.status_code == 201
        assert response.text == '{"ok":true}'
        response = requests.post(f'{URL}/api/v1/courier', data=payload)
        assert response.status_code == 409
        response = requests.post(f'{URL}/api/v1/courier/login', data=payload)
        path = response.json()["id"]
        response = requests.delete(f'{URL}/api/v1/courier/{path}')
        response = requests.post(f'{URL}/api/v1/courier/login', data=payload)

    @allure.step('Проверка создания курьера с незаполненным полем логин')
    def test_register_couriers_empty_field_login(self):
        payload = {
            "password": ps,
            "firstName": fn
        }
        response = requests.post(f'{URL}/api/v1/courier',
                                 data=payload)
        assert response.status_code == 400

    @allure.step('Проверка создания курьера с незаполненным полем пароль')
    def test_register_couriers_empty_field_password(self):
        payload = {
            "login": lg,
            "firstName": fn
        }
        response = requests.post(f'{URL}/api/v1/courier',
                                 data=payload)
        assert response.status_code == 400

    @allure.step('Проверка создания курьера с незаполненным полем имя')
    def test_register_couriers_empty_field_firstname(self):
        payload = {
            "login": lg,
            "password": ps
        }
        response = requests.post(f'{URL}/api/v1/courier', data=payload)
        assert response.status_code == 201
        response = requests.post(f'{URL}/api/v1/courier/login', data=payload)
        path = response.json()["id"]
        response = requests.delete(f'{URL}/api/v1/courier/{path}')
        response = requests.post(f'{URL}/api/v1/courier/login', data=payload)

    @allure.step('Проверка создания курьера с уже использующимся логином')
    def test_register_couriers_with_login_used(self):
        payload = {
            "login": lg,
            "password": ps
        }
        payload1 = {
            "login": lg,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(f'{URL}/api/v1/courier', data=payload)
        response = requests.post(f'{URL}/api/v1/courier', data=payload1)
        assert response.status_code == 409
        response = requests.post(f'{URL}/api/v1/courier/login', data=payload)
        path = response.json()["id"]
        response = requests.delete(f'{URL}/api/v1/courier/{path}')
        response = requests.post(f'{URL}/api/v1/courier/login', data=payload)
