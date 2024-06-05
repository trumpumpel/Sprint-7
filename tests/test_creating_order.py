import allure
import requests
import pytest

from data import lg, ps, fn, URL


class TestCreatingOrder:

    @allure.title('Проверка работы создания заказа с помощью параметризации')
    @allure.step('Проверка наличия track  в ответе при создании заказа.')
    @pytest.mark.parametrize(
        'firstname, lastname, address, metrostation, phone, renttime, deliverydate, comment, color',
        [
            ["Duncan", "MacLeod", "SW1A 0AA", "Westminster", "+74954261754", 4, "21.06.2024", "viva chile", "BLACK"],
            ['', 'MacLeod', 'SW1A 0AA', 'Westminster', '+74954261754', '4', '21.06.2024', 'viva chile', 'BLACK'],
            ['Duncan', '', 'SW1A 0AA', 'Westminster', '+74954261754', '4', '21.06.2024', 'viva chile', 'BLACK'],
            ['Duncan', 'MacLeod', '', 'Westminster', '+74954261754', '4', '21.06.2024', 'viva chile', 'BLACK'],
            ['Duncan', 'MacLeod', 'SW1A 0AA', '', '+74954261754', '4', '21.06.2024', 'viva chile', 'BLACK'],
            ['Duncan', 'MacLeod', 'SW1A 0AA', 'Westminster', '', '4', '21.06.2024', 'viva chile', 'BLACK'],
            ['Duncan', 'MacLeod', 'SW1A 0AA', 'Westminster', '+74954261754', '', '21.06.2024', 'viva chile', 'BLACK'],
            ['Duncan', 'MacLeod', 'SW1A 0AA', 'Westminster', '+74954261754', '4', '', 'viva chile', 'BLACK'],
            ['Duncan', 'MacLeod', 'SW1A 0AA', 'Westminster', '+74954261754', '4', '21.06.2024', 'viva chile',
             'BLACKGREY'],
            ['Duncan', 'MacLeod', 'SW1A 0AA', 'Westminster', '+74954261754', '4', '21.06.2024', 'viva chile',
             'BLACKGREY'],
            ['Duncan', 'MacLeod', 'SW1A 0AA', 'Westminster', '+74954261754', '4', '21.06.2024', 'viva chile', ''],
            ['Duncan', 'MacLeod', 'SW1A 0AA', 'Westminster', '+74954261754', '4', '21.06.2024', 'viva chile', 'GREY']
        ]
    )
    def test_creating_order(self, firstname, lastname, address, metrostation, phone, renttime, deliverydate, comment,
                            color):
        response = requests.post(f'{URL}/api/v1/orders')
        assert response.status_code == 201
        assert 'track' in response.text
        path = response.json()["track"]
        response_find = requests.get(f'{URL}/api/v1/orders/track?t={path}')
        assert response_find.status_code == 200

    @allure.step('Проверка наличия созданного заказа в списке заказов.')
    def test_getting_list_of_orders(self):
        payload = {
            "login": lg,
            "password": ps,
            "firstName": fn
        }
        data = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Saske, come back to Konoha",
            "color": [
                "BLACK"
            ]

        }
        response = requests.post(f'{URL}/api/v1/courier', data=payload)
        response = requests.post(f'{URL}/api/v1/orders', json=data)
        track = response.json()["track"]
        response_id_c = requests.post(f'{URL}/api/v1/courier/login', data=payload)
        id_c = response_id_c.json()["id"]
        response = requests.get(f'{URL}/api/v1/orders/accept/{track}?courierId={id_c}')
        response = requests.delete(f'{URL}/api/v1/courier/{id_c}')
        response = requests.post(f'{URL}/api/v1/courier/login', data=payload)
        assert response.status_code == 404
