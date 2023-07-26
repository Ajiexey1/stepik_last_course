import pytest
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage

Url_For_Product_Page = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


def test_guest_can_add_product_to_basket(browser):
    link = Url_For_Product_Page
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_basket()  # Добавляем товар в корзину


@pytest.mark.skip
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


@pytest.mark.skip
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


@pytest.mark.test
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = Url_For_Product_Page
    page = BasketPage(browser, link)
    page.open()
    page.open_basket()  # Открываем корзину
    page.empty_shopping_list()
    page.empty_shopping_list_text()

@pytest.mark.test
def test_guest_can_see_product_in_basket(browser):
    link = Url_For_Product_Page
    page1 = ProductPage(browser, link)
    page1.open()
    page1.add_to_basket()  # Добавляем товар в корзину
    page2 = BasketPage(browser, link)
    page2.open_basket()  # Открываем корзину
    page2.not_empty_shopping_text()
