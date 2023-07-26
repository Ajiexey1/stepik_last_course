from .pages.main_page import MainPage
from .pages.basket_page import BasketPage

Main_Page_Url = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_go_to_login_page(browser):
    link = Main_Page_Url
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = Main_Page_Url
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = Main_Page_Url
    page = BasketPage(browser, link)
    page.open()
    page.open_basket()
    page.empty_shopping_list()
    page.empty_shopping_list_text()
