import string
import random

lg = "murfl"
ps = '234634'
fn = "burfl"


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


login = generate_random_string(10)
password = generate_random_string(10)
first_name = generate_random_string(10)

URL = "https://qa-scooter.praktikum-services.ru"
PATH_COURIER = "/api/v1/courier"
PATH_LOGIN = "/api/v1/courier/login"
PATH_ORDERS = "/api/v1/orders"
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
payload1 = {
    "login": lg,
    "password": password,
    "firstName": first_name
}
payload2 = {
    "login": login,
    "password": password,
    "firstName": first_name
}
payload3 = {
    "login": lg,
    "firstName": fn
}
payload4 = {
    "login": lg,
    "password": ps
}
payload5 = {
    "login": lg,
    "password": ''
}
payload6 = {
    "login": '',
    "password": ps
}
payload7 = {
    "password": ps,
    "firstName": fn
}
