import requests
import pytest
import allure
import json
import random
import string

from data import lg, ps, fn, URL
from helpers import login, password, first_name, login_pass


class TestCourier:
    # метод регистрации нового курьера возвращает список из логина и пароля
    # если регистрация не удалась, возвращает пустой список
    def test_register_new_courier_and_return_login_password(self):
        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        # возвращаем список
        return login_pass

    def test_register_two_couriers(self):
        # собираем тело запроса
        payload = {
            "login": lg,
            "password": ps,
            "firstName": fn
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post(f'{URL}/api/v1/courier', data=payload)
        assert response.status_code == 201
        assert response.text == '{"ok":true}'
        response = requests.post(f'{URL}/api/v1/courier', data=payload)
        assert response.status_code == 409
        response = requests.post(f'{URL}/api/v1/courier/login', data=payload)
        assert response.status_code == 200
        path = response.json()["id"]
        response_delete = requests.delete(f'{URL}/api/v1/courier/{path}')
        assert response_delete.status_code == 200
        response = requests.post(f'{URL}/api/v1/courier/login', data=payload)
        assert response.status_code == 404

    def test_register_couriers_empty_field_login(self):
        payload = {
            "password": ps,
            "firstName": fn
        }
        response = requests.post(f'{URL}/api/v1/courier',
                                 data=payload)
        assert response.status_code == 400
        print(response.text)

    def test_register_couriers_empty_field_password(self):
        payload = {
            "login": lg,
            "firstName": fn
        }
        response = requests.post(f'{URL}/api/v1/courier',
                                 data=payload)
        assert response.status_code == 400

    def test_register_couriers_empty_field_firstname(self):
        payload = {
            "login": lg,
            "password": ps
        }
        response = requests.post(f'{URL}/api/v1/courier',
                                 data=payload)
        assert response.status_code == 201
        response = requests.post(f'{URL}/api/v1/courier/login', data=payload)
        assert response.status_code == 200
        path = response.json()["id"]
        response_delete = requests.delete(f'{URL}/api/v1/courier/{path}')
        assert response_delete.status_code == 200
        response = requests.post(f'{URL}/api/v1/courier/login', data=payload)
        assert response.status_code == 404
