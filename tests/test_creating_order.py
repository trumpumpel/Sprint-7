import allure
import requests
import pytest

from data import URL, PATH_LOGIN, PATH_ORDERS, PATH_COURIER, data, payload


class TestCreatingOrder:

    @allure.title('Проверка работы создания заказа с помощью параметризации')
    @allure.step('Проверка наличия track  в ответе при создании заказа.')
    @pytest.mark.parametrize(
        'firstname, lastname, address, metrostation, phone, renttime, deliverydate, comment, color',

        [
            ['Duncan', 'MacLeod', 'SW1A 0AA', 'Westminster', '+74954261754', '4', '21.06.2024', 'viva chile',
             'BLACK'],
            ['Duncan', 'MacLeod', 'SW1A 0AA', 'Westminster', '+74954261754', '4', '21.06.2024', 'viva chile',
             'GREY'],
            ['Duncan', 'MacLeod', 'SW1A 0AA', 'Westminster', '+74954261754', '4', '21.06.2024', 'viva chile',
             'BLACK''GREY'],
            ['Duncan', 'MacLeod', 'SW1A 0AA', 'Westminster', '+74954261754', '4', '21.06.2024', 'viva chile', '']
        ]
    )
    def test_creating_order(self, firstname, lastname, address, metrostation, phone, renttime, deliverydate,
                            comment,
                            color):
        response = requests.post(f'{URL}{PATH_ORDERS}')
        assert response.status_code == 201
        assert 'track' in response.text

    @allure.title('Проверка наличия созданного заказа в списке заказов.')
    def test_getting_list_of_orders(self):
        requests.post(f'{URL}{PATH_COURIER}', data=payload)
        response = requests.post(f'{URL}{PATH_ORDERS}', json=data)
        track = response.json()["track"]
        response_id_c = requests.post(f'{URL}{PATH_LOGIN}', data=payload)
        id_c = response_id_c.json()["id"]
        requests.get(f'{URL}{PATH_ORDERS}/accept/{track}?courierId={id_c}')
        requests.delete(f'{URL}{PATH_COURIER}/{id_c}')
        response = requests.post(f'{URL}{PATH_LOGIN}', data=payload)
        assert response.status_code == 404
