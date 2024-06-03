import requests
import pytest
import allure
import json
import random
import string

from data import lg, ps, fn, FIRSTNAME, METROSTATION, ADDRESS, LASTNAME, PHONE, RENTTIME, DELIVERYDATE, COMMENT, COLOR1, \
    COLOR2
from helpers import login, password, first_name, login_pass


class TestCreatingOrder:
    def test_creating_order(self):
        payload = {FIRSTNAME, LASTNAME, ADDRESS, METROSTATION, PHONE, RENTTIME, DELIVERYDATE, COMMENT, COLOR1}

        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', data=payload)
        assert response.status_code == 201
        print(response.text)
        path = response.json()["track"]
        response_delete = requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{path}')
        assert response_delete.status_code == 200
