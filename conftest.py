import pytest
from selenium import webdriver
from data import URL
import allure


@allure.step('Открываем браузер Firefox')
def browser_settings():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--window-size=1920, 990')
    return firefox_options


@allure.step('Открываем страницу {page}')
@pytest.fixture
def driver():
    firefox = webdriver.Firefox()
    firefox.get(URL)
    yield firefox
    firefox.quit()
