import allure
import requests

from data import lg, ps, url
from conftest import payload2, payload5, payload6, user_registration_and_delete, payload


class TestLoginCourier:
    @allure.title('Проверка алгоритмов авторизации курьера')
    @allure.title('Проверка авторизации курьера.')
    def test_courier_authorization(self):
        response = requests.post(f'{url}/api/v1/courier', data=payload)
        assert response.text == '{"ok":true}'
        response = requests.post(f'{url}/api/v1/courier/login', data=payload)
        path = response.json()["id"]
        requests.delete(f'{url}/api/v1/courier/{path}')
        requests.post(f'{url}/api/v1/courier/login', data=payload)

    @allure.title('Проверка авторизации курьера с незаполненным полем логин.')
    def test_courier_authorization_empty_field_login(self, user_registration_and_delete):
        response = requests.post(f'{url}/api/v1/courier/login', data=payload6)
        assert response.status_code == 400

    @allure.title('Проверка авторизации курьера с незаполненным полем пароль.')
    def test_courier_authorization_empty_field_password(self, user_registration_and_delete):
        response = requests.post(f'{url}/api/v1/courier/login', data=payload5)
        assert response.status_code == 400

    @allure.title('Проверка авторизации незарегистрированного курьера.')
    def test_authorization_non_existent_user(self):
        response = requests.post(f'{url}/api/v1/courier/login', data=payload2)
        assert response.status_code == 404

    @allure.title('Проверка возврата id в случае успешного запроса.')
    def test_id_return(self, user_registration_and_delete):
        response = requests.post(f'{url}/api/v1/courier/login', data=payload)
        assert 'id' in response.text
