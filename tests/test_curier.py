import allure
import requests

from data import lg, ps, fn, url
from conftest import password, first_name, user_registration_and_delete, payload, payload4


class TestCourier:

    @allure.title('Проверка алгоритмов создания курьера')
    @allure.step('Проверка создания курьера и двух с одинаковыми данными')
    def test_register_two_couriers(self, user_registration_and_delete):
        response = requests.post(f'{url}/api/v1/courier', data=payload)
        assert response.status_code == 409

    @allure.step('Проверка создания курьера с незаполненным полем логин')
    def test_register_couriers_empty_field_login(self):
        payload2 = {
            "password": ps,
            "firstName": fn
        }
        response = requests.post(f'{url}/api/v1/courier',
                                 data=payload2)
        assert response.status_code == 400

    @allure.step('Проверка создания курьера с незаполненным полем пароль')
    def test_register_couriers_empty_field_password(self):
        payload3 = {
            "login": lg,
            "firstName": fn
        }
        response = requests.post(f'{url}/api/v1/courier',
                                 data=payload3)
        assert response.status_code == 400

    @allure.step('Проверка создания курьера с незаполненным полем имя')
    def test_register_couriers_empty_field_firstname(self):
        response = requests.post(f'{url}/api/v1/courier', data=payload4)
        assert response.status_code == 201
        response = requests.post(f'{url}/api/v1/courier/login', data=payload4)
        path = response.json()["id"]
        requests.delete(f'{url}/api/v1/courier/{path}')
        requests.post(f'{url}/api/v1/courier/login', data=payload4)

    @allure.step('Проверка создания курьера с уже использующимся логином')
    def test_register_couriers_with_login_used(self, user_registration_and_delete):
        payload1 = {
            "login": lg,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(f'{url}/api/v1/courier', data=payload1)
        assert response.status_code == 409

    def test_reg(self, user_registration_and_delete):
        payload1 = {
            "login": lg,
            "password": password,
            "firstName": first_name
        }
        response = requests.post(f'{url}/api/v1/courier', data=payload1)
        assert response.status_code == 409
