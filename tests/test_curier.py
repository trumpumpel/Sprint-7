import allure
import requests
from data.test_url_data import TestUrlData
from data.test_auth_data import TestAuthData
from conftest import user_registration_and_delete


class TestCourier:

    @allure.title('Проверка алгоритмов создания курьера')
    @allure.title('Проверка создания курьера')
    def test_register_courier(self):
        requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_COURIER}', data=TestAuthData.payload)
        response = requests.post(f"{TestUrlData.URL}{TestUrlData.PATH_LOGIN}", data=TestAuthData.payload)
        assert response.status_code == 200
        path = response.json()["id"]
        requests.delete(f'{TestUrlData.URL}{TestUrlData.PATH_COURIER}/{path}')
        requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_LOGIN}', data=TestAuthData.payload)

    @allure.title('Проверка создания курьера и двух с одинаковыми данными')
    def test_register_two_couriers(self, user_registration_and_delete):
        response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_COURIER}', data=TestAuthData.payload)
        assert response.status_code == 409

    @allure.title('Проверка создания курьера с незаполненным полем логин')
    def test_register_couriers_empty_field_login(self):
        response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_COURIER}',
                                 data=TestAuthData.payload_register_couriers_empty_field_login)
        assert response.status_code == 400

    @allure.title('Проверка создания курьера с незаполненным полем пароль')
    def test_register_couriers_empty_field_password(self):
        response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_COURIER}',
                                 data=TestAuthData.payload_register_couriers_empty_field_password)
        assert response.status_code == 400

    @allure.title('Проверка создания курьера с незаполненным полем имя')
    def test_register_couriers_empty_field_firstname(self):
        response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_COURIER}',
                                 data=TestAuthData.payload_register_couriers_empty_field_firstname)
        assert response.status_code == 201
        response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_LOGIN}',
                                 data=TestAuthData.payload_register_couriers_empty_field_firstname)
        path = response.json()["id"]
        requests.delete(f'{TestUrlData.URL}{TestUrlData.PATH_COURIER}{path}')
        requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_LOGIN}',
                      data=TestAuthData.payload_register_couriers_empty_field_firstname)

    @allure.title('Проверка создания курьера с уже использующимся логином')
    def test_register_couriers_with_login_used(self, user_registration_and_delete):
        response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_COURIER}',
                                 data=TestAuthData.payload_register_couriers_with_login_used)
        assert response.status_code == 409

    @allure.title('Проверка возврата {"ok":true} в случае успешного запроса')
    def test_register_courier_answer_ok_true(self, user_registration_and_delete):
        response = requests.post(f'{TestUrlData.URL}{TestUrlData.PATH_COURIER}', data=TestAuthData.payload)
        assert '{"ok":true}' not in response.text

    @allure.title('Проверка возврата правильного кода в случае успешного запроса')
    def test_register_couriers_answer_correct(self):
        response = requests.post(f"{TestUrlData.URL}{TestUrlData.PATH_LOGIN}", data=TestAuthData.payload)
        assert response.status_code == 404

# class TestCourier:
#
#     @allure.title('Проверка алгоритмов создания курьера')
#     @allure.title('Проверка создания курьера')
#     def test_register_courier(self):
#         requests.post(f'{URL}{PATH_COURIER}', data=payload)
#         response = requests.post(f"{URL}{PATH_LOGIN}", data=payload)
#         assert response.status_code == 200
#         path = response.json()["id"]
#         requests.delete(f'{URL}{PATH_COURIER}/{path}')
#         requests.post(f'{URL}{PATH_LOGIN}', data=payload)
#
#     @allure.title('Проверка создания курьера и двух с одинаковыми данными')
#     def test_register_two_couriers(self, user_registration_and_delete):
#         response = requests.post(f'{URL}{PATH_COURIER}', data=payload)
#         assert response.status_code == 409
#
#     @allure.title('Проверка создания курьера с незаполненным полем логин')
#     def test_register_couriers_empty_field_login(self):
#         response = requests.post(f'{URL}{PATH_COURIER}',
#                                  data=payload_register_couriers_empty_field_login)
#         assert response.status_code == 400
#
#     @allure.title('Проверка создания курьера с незаполненным полем пароль')
#     def test_register_couriers_empty_field_password(self):
#         response = requests.post(f'{URL}{PATH_COURIER}',
#                                  data=payload_register_couriers_empty_field_password)
#         assert response.status_code == 400
#
#     @allure.title('Проверка создания курьера с незаполненным полем имя')
#     def test_register_couriers_empty_field_firstname(self):
#         response = requests.post(f'{URL}{PATH_COURIER}', data=payload_register_couriers_empty_field_firstname)
#         assert response.status_code == 201
#         response = requests.post(f'{URL}{PATH_LOGIN}', data=payload_register_couriers_empty_field_firstname)
#         path = response.json()["id"]
#         requests.delete(f'{URL}{PATH_COURIER}{path}')
#         requests.post(f'{URL}{PATH_LOGIN}', data=payload_register_couriers_empty_field_firstname)
#
#     @allure.title('Проверка создания курьера с уже использующимся логином')
#     def test_register_couriers_with_login_used(self, user_registration_and_delete):
#         response = requests.post(f'{URL}{PATH_COURIER}', data=payload_register_couriers_with_login_used)
#         assert response.status_code == 409
#
#     @allure.title('Проверка возврата {"ok":true} в случае успешного запроса')
#     def test_register_courier_answer_ok_true(self, user_registration_and_delete):
#         response = requests.post(f'{URL}{PATH_COURIER}', data=payload)
#         assert '{"ok":true}' not in response.text
#
#     @allure.title('Проверка возврата правильного кода в случае успешного запроса')
#     def test_register_couriers_answer_correct(self):
#         response = requests.post(f"{URL}{PATH_LOGIN}", data=payload)
#         assert response.status_code == 404
