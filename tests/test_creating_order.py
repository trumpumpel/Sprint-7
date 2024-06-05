import requests
import pytest
import allure
import json
import random
import string

from data import lg, ps, fn, FIRSTNAME, METROSTATION, ADDRESS, LASTNAME, PHONE, RENTTIME, DELIVERYDATE, COMMENT, COLOR1, \
    COLOR2, URL
from helpers import login, password, first_name, login_pass


class TestCreatingOrder:
    def test_creating_order(self):
        payload = {FIRSTNAME, LASTNAME, ADDRESS, METROSTATION, PHONE, RENTTIME, DELIVERYDATE, COMMENT, COLOR1}

        response = requests.post(f'{URL}/orders', data=payload)
        assert response.status_code == 201
        print(response.text)
        path = response.json()["track"]
        response_delete = requests.delete(f'{URL}/{path}')
        assert response_delete.status_code == 200
