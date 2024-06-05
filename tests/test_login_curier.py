import allure
import requests

from data import lg, ps, URL
from helpers import login, password


class TestLoginCourier:
    @allure.title('Проверка алгоритмов авторизации курьера')
    @allure.step('Проверка авторизации курьера.')
    def test_courier_authorization(self):
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

    @allure.step('Проверка авторизации курьера с незаполненным полем логин.')
    def test_courier_authorization_empty_field_login(self):
        payload = {
            "login": lg,
            "password": ps
        }
        payload1 = {
            "login": '',
            "password": ps
        }

        response = requests.post(f'{URL}/api/v1/courier', data=payload)
        response = requests.post(f'{URL}/api/v1/courier/login', data=payload1)
        assert response.status_code == 400
        response = requests.post(f'{URL}/api/v1/courier/login', data=payload)
        path = response.json()["id"]
        response = requests.delete(f'{URL}/api/v1/courier/{path}')
        response = requests.post(f'{URL}/api/v1/courier/login', data=payload)

    @allure.step('Проверка авторизации курьера с незаполненным полем пароль.')
    def test_courier_authorization_empty_field_password(self):
        payload = {
            "login": lg,
            "password": ps
        }

        payload1 = {
            "login": lg,
            "password": ''
        }

        response = requests.post(f'{URL}/api/v1/courier', data=payload)
        response = requests.post(f'{URL}/api/v1/courier/login', data=payload1)
        assert response.status_code == 400
        response = requests.post(f'{URL}/api/v1/courier/login', data=payload)
        path = response.json()["id"]
        response = requests.delete(f'{URL}/api/v1/courier/{path}')
        response = requests.post(f'{URL}/api/v1/courier/login', data=payload)

    @allure.step('Проверка авторизации незарегистрированного курьера.')
    def test_authorization_non_existent_user(self):
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(f'{URL}/api/v1/courier/login', data=payload)
        assert response.status_code == 404

    @allure.step('Проверка возврата id в случае успешного запроса.')
    def test_id_return(self):
        payload = {
            "login": lg,
            "password": ps
        }
        response = requests.post(f'{URL}/api/v1/courier', data=payload)
        response = requests.post(f'{URL}/api/v1/courier/login', data=payload)
        assert 'id' in response.text
        path = response.json()["id"]
        response = requests.delete(f'{URL}/api/v1/courier/{path}')
        response = requests.post(f'{URL}/api/v1/courier/login', data=payload)
