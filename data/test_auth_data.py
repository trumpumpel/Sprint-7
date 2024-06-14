from helpers import login, password, first_name


class TestAuthData:
    lg = "murfl"
    ps = '234634'
    fn = "burfl"

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
    payload = {
        "login": lg,
        "password": ps,
        "firstName": fn
    }
    payload_register_couriers_with_login_used = {
        "login": lg,
        "password": password,
        "firstName": first_name
    }
    payload_authorization_non_existent_user = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    payload_register_couriers_empty_field_password = {
        "login": lg,
        "firstName": fn
    }
    payload_register_couriers_empty_field_firstname = {
        "login": lg,
        "password": ps
    }
    payload_courier_authorization_empty_field_password = {
        "login": lg,
        "password": ''
    }
    payload_courier_authorization_empty_field_login = {
        "login": '',
        "password": ps
    }
    payload_register_couriers_empty_field_login = {
        "password": ps,
        "firstName": fn
    }
