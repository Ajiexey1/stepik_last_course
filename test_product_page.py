import pytest

from .pages.product_page import ProductPage

Url_For_Product_Page = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser):
    link = Url_For_Product_Page
    page = ProductPage(browser,
                       link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_to_basket()  # Добавляем товар в корзину


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


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = Url_For_Product_Page
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()  # Добавляем товар в корзину
    page.should_disappeared()  # Проверяем, что уведомление о покупке не исчезает
