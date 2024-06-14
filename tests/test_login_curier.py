import allure
import requests

from data.test_url_data import TestUrlData
from data.test_auth_data import TestAuthData
from conftest import user_registration_and_delete


class TestLoginCourier:
    @allure.title('Проверка алгоритмов авторизации курьера')
    @allure.title('Проверка авторизации курьера.')
    def test_courier_authorization(self):
        response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_COURIER}', data=TestAuthData.payload)
        assert '{"ok":true}' in response.text
        response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_LOGIN}', data=TestAuthData.payload)
        path = response.json()["id"]
        requests.delete(f'{TestUrlData.URL}{TestUrlData.PATH_COURIER}/{path}')
        requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_LOGIN}', data=TestAuthData.payload)

    @allure.title('Проверка авторизации курьера с незаполненным полем логин.')
    def test_courier_authorization_empty_field_login(self, user_registration_and_delete):
        response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_LOGIN}',
                                 data=TestAuthData.payload_courier_authorization_empty_field_login)
        assert response.status_code == 400

    @allure.title('Проверка авторизации курьера с незаполненным полем пароль.')
    def test_courier_authorization_empty_field_password(self, user_registration_and_delete):
        response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_LOGIN}',
                                 data=TestAuthData.payload_courier_authorization_empty_field_password)
        assert response.status_code == 400

    @allure.title('Проверка авторизации незарегистрированного курьера.')
    def test_authorization_non_existent_user(self):
        response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_LOGIN}',
                                 data=TestAuthData.payload_authorization_non_existent_user)
        assert response.status_code == 404

    @allure.title('Проверка возврата id в случае успешного запроса.')
    def test_id_return(self, user_registration_and_delete):
        response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_LOGIN}', data=TestAuthData.payload)
        assert 'id' in response.text
