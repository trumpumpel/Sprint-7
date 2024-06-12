import allure
import requests

from data import URL, PATH_COURIER, PATH_LOGIN, payload_courier_authorization_empty_field_login, payload_courier_authorization_empty_field_password, payload, \
    payload_authorization_non_existent_user
from conftest import user_registration_and_delete


class TestLoginCourier:
    @allure.title('Проверка алгоритмов авторизации курьера')
    @allure.title('Проверка авторизации курьера.')
    def test_courier_authorization(self):
        response = requests.post(f'{URL}{PATH_COURIER}', data=payload)
        assert '{"ok":true}' in response.text
        response = requests.post(f'{URL}{PATH_LOGIN}', data=payload)
        path = response.json()["id"]
        requests.delete(f'{URL}{PATH_COURIER}/{path}')
        requests.post(f'{URL}{PATH_LOGIN}', data=payload)

    @allure.title('Проверка авторизации курьера с незаполненным полем логин.')
    def test_courier_authorization_empty_field_login(self, user_registration_and_delete):
        response = requests.post(f'{URL}{PATH_LOGIN}', data=payload_courier_authorization_empty_field_login)
        assert response.status_code == 400

    @allure.title('Проверка авторизации курьера с незаполненным полем пароль.')
    def test_courier_authorization_empty_field_password(self, user_registration_and_delete):
        response = requests.post(f'{URL}{PATH_LOGIN}', data=payload_courier_authorization_empty_field_password)
        assert response.status_code == 400

    @allure.title('Проверка авторизации незарегистрированного курьера.')
    def test_authorization_non_existent_user(self):
        response = requests.post(f'{URL}{PATH_LOGIN}', data=payload_authorization_non_existent_user)
        assert response.status_code == 404

    @allure.title('Проверка возврата id в случае успешного запроса.')
    def test_id_return(self, user_registration_and_delete):
        response = requests.post(f'{URL}{PATH_LOGIN}', data=payload)
        assert 'id' in response.text
