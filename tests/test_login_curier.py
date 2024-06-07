import allure
import requests

from data import lg, ps, url
# from helpers import login, password
from conftest import password, login
from conftest import password, first_name, user_registration_and_delete, payload, payload4, data, user_registration


class TestLoginCourier:
    @allure.title('Проверка алгоритмов авторизации курьера')
    @allure.step('Проверка авторизации курьера.')
    def test_courier_authorization(self):
        # payload = {
        #     "login": lg,
        #     "password": ps
        # }

        response = requests.post(f'{url}/api/v1/courier', data=payload)
        assert response.text == '{"ok":true}'
        response = requests.post(f'{url}/api/v1/courier/login', data=payload)
        path = response.json()["id"]
        requests.delete(f'{url}/api/v1/courier/{path}')
        requests.post(f'{url}/api/v1/courier/login', data=payload)

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

        requests.post(f'{url}/api/v1/courier', data=payload)
        response = requests.post(f'{url}/api/v1/courier/login', data=payload1)
        assert response.status_code == 400
        response = requests.post(f'{url}/api/v1/courier/login', data=payload)
        path = response.json()["id"]
        requests.delete(f'{url}/api/v1/courier/{path}')
        requests.post(f'{url}/api/v1/courier/login', data=payload)

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

        requests.post(f'{url}/api/v1/courier', data=payload)
        response = requests.post(f'{url}/api/v1/courier/login', data=payload1)
        assert response.status_code == 400
        response = requests.post(f'{url}/api/v1/courier/login', data=payload)
        path = response.json()["id"]
        requests.delete(f'{url}/api/v1/courier/{path}')
        requests.post(f'{url}/api/v1/courier/login', data=payload)

    @allure.step('Проверка авторизации незарегистрированного курьера.')
    def test_authorization_non_existent_user(self):
        payload = {
            "login": login,
            "password": password
        }
        response = requests.post(f'{url}/api/v1/courier/login', data=payload)
        assert response.status_code == 404

    @allure.step('Проверка возврата id в случае успешного запроса.')
    def test_id_return(self):
        payload = {
            "login": lg,
            "password": ps
        }
        requests.post(f'{url}/api/v1/courier', data=payload)
        response = requests.post(f'{url}/api/v1/courier/login', data=payload)
        assert 'id' in response.text
        path = response.json()["id"]
        requests.delete(f'{url}/api/v1/courier/{path}')
        requests.post(f'{url}/api/v1/courier/login', data=payload)
