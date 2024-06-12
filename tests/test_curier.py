import allure
import requests
from conftest import user_registration_and_delete
from data import payload, payload4, payload3, payload1, payload7, URL, PATH_COURIER, PATH_LOGIN


class TestCourier:

    @allure.title('Проверка алгоритмов создания курьера')
    @allure.title('Проверка создания курьера')
    def test_register_courier(self):
        requests.post(f'{URL}{PATH_COURIER}', data=payload)
        response = requests.post(f"{URL}{PATH_LOGIN}", data=payload)
        assert response.status_code == 200
        path = response.json()["id"]
        requests.delete(f'{URL}{PATH_COURIER}/{path}')
        requests.post(f'{URL}{PATH_LOGIN}', data=payload)

    @allure.title('Проверка создания курьера и двух с одинаковыми данными')
    def test_register_two_couriers(self, user_registration_and_delete):
        response = requests.post(f'{URL}{PATH_COURIER}', data=payload)
        assert response.status_code == 409

    @allure.title('Проверка создания курьера с незаполненным полем логин')
    def test_register_couriers_empty_field_login(self):
        response = requests.post(f'{URL}{PATH_COURIER}',
                                 data=payload7)
        assert response.status_code == 400

    @allure.title('Проверка создания курьера с незаполненным полем пароль')
    def test_register_couriers_empty_field_password(self):
        response = requests.post(f'{URL}{PATH_COURIER}',
                                 data=payload3)
        assert response.status_code == 400

    @allure.title('Проверка создания курьера с незаполненным полем имя')
    def test_register_couriers_empty_field_firstname(self):
        response = requests.post(f'{URL}{PATH_COURIER}', data=payload4)
        assert response.status_code == 201
        response = requests.post(f'{URL}{PATH_LOGIN}', data=payload4)
        path = response.json()["id"]
        requests.delete(f'{URL}{PATH_COURIER}{path}')
        requests.post(f'{URL}{PATH_LOGIN}', data=payload4)

    @allure.title('Проверка создания курьера с уже использующимся логином')
    def test_register_couriers_with_login_used(self, user_registration_and_delete):
        response = requests.post(f'{URL}{PATH_COURIER}', data=payload1)
        assert response.status_code == 409

    @allure.title('Проверка возврата {"ok":true} в случае успешного запроса')
    def test_register_courier_answer_ok_true(self, user_registration_and_delete):
        response = requests.post(f'{URL}{PATH_COURIER}', data=payload)
        assert '{"ok":true}' not in response.text

    @allure.title('Проверка возврата правильного кода в случае успешного запроса')
    def test_register_couriers_answer_correct(self):
        response = requests.post(f"{URL}{PATH_LOGIN}", data=payload)
        assert response.status_code == 404
