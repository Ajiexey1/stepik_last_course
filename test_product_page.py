import time

import faker
import pytest
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage

Url_For_Product_Page = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
Login_Url = "https://selenium1py.pythonanywhere.com/accounts/login/"


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = Url_For_Product_Page
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_basket()  # Добавляем товар в корзину


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = Url_For_Product_Page
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()  # Добавляем товар в корзину
    page.should_not_be_success_message()  # Проверяем, что нет уведомления о покупке


def test_guest_cant_see_success_message(browser):
    link = Url_For_Product_Page
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()  # Проверяем, что нет уведомления о покупке


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = Url_For_Product_Page
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()  # Добавляем товар в корзину
    page.should_disappeared()  # Проверяем, что уведомление о покупке не исчезает


def test_guest_should_see_login_link_on_product_page(browser):
    link = Url_For_Product_Page
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.xfail
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = Url_For_Product_Page
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = Url_For_Product_Page
    page = BasketPage(browser, link)
    page.open()
    page.open_basket()  # Открываем корзину
    page.empty_shopping_list()
    page.empty_shopping_list_text()


@pytest.mark.need_review
def test_guest_can_see_product_in_basket(browser):
    link = Url_For_Product_Page
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()  # Добавляем товар в корзину
    page = BasketPage(browser, link)
    page.open_basket()  # Открываем корзину
    page.not_empty_shopping_text()


@pytest.mark.reg_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = Login_Url
        page = LoginPage(browser, link)
        page.open()
        f = faker.Faker()
        email = f.email()
        password = str(time.time())
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = Url_For_Product_Page
        page = ProductPage(browser,
                           link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.add_to_basket()  # Добавляем товар в корзину

    def test_user_cant_see_success_message(self, browser):
        link = Url_For_Product_Page
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()  # Проверяем, что нет уведомления о покупке
