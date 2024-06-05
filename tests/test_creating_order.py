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

    @pytest.mark.parametrize(
        'FIRSTNAME, LASTNAME, ADDRESS, METROSTATION, PHONE, RENTTIME, DELIVERYDATE, COMMENT, COLOR',
        [
            ['Duncan', 'MacLeod', 'SW1A 0AA', 'Westminster', '+74954261754', '4', '21.06.2024', 'viva chile', 'BLACK'],
            ['', 'MacLeod', 'SW1A 0AA', 'Westminster', '+74954261754', '4', '21.06.2024', 'viva chile', 'BLACK'],
            ['Duncan', '', 'SW1A 0AA', 'Westminster', '+74954261754', '4', '21.06.2024', 'viva chile', 'BLACK'],
            ['Duncan', 'MacLeod', '', 'Westminster', '+74954261754', '4', '21.06.2024', 'viva chile', 'BLACK'],
            ['Duncan', 'MacLeod', 'SW1A 0AA', '', '+74954261754', '4', '21.06.2024', 'viva chile', 'BLACK'],
            ['Duncan', 'MacLeod', 'SW1A 0AA', 'Westminster', '', '4', '21.06.2024', 'viva chile', 'BLACK'],
            ['Duncan', 'MacLeod', 'SW1A 0AA', 'Westminster', '+74954261754', '', '21.06.2024', 'viva chile', 'BLACK'],
            ['Duncan', 'MacLeod', 'SW1A 0AA', 'Westminster', '+74954261754', '4', '', 'viva chile', 'BLACK'],
            ['Duncan', 'MacLeod', 'SW1A 0AA', 'Westminster', '+74954261754', '4', '', 'viva chile', 'BLACKGREY'],
            ['Duncan', 'MacLeod', 'SW1A 0AA', 'Westminster', '+74954261754', '4', '', 'viva chile', 'BLACKGREY'],
            ['Duncan', 'MacLeod', 'SW1A 0AA', 'Westminster', '+74954261754', '4', '', 'viva chile', ''],
            ['Duncan', 'MacLeod', 'SW1A 0AA', 'Westminster', '+74954261754', '4', '21.06.2024', 'viva chile', 'GREY']
        ]
    )
    def test_creating_order(self):
        # payload = {LASTNAME, LASTNAME, LASTNAME, LASTNAME, PHONE, RENTTIME, DELIVERYDATE, COMMENT, COLOR1}

        response = requests.post(f'{URL}/orders', data=pytest.mark.parametrize)
        assert response.status_code == 201
        print(response.text)
        path = response.json()["track"]
        # response_delete = requests.delete(f'{URL}/{path}')
        # assert response_delete.status_code == 200
