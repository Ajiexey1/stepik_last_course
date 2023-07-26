import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        login_link.click()
        # self.solve_quiz_and_get_code()
        # time.sleep(5)
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        item_name_in_basket = self.browser.find_element(*ProductPageLocators.ITEM_NAME_IN_BASKET).text
        assert item_name == item_name_in_basket, 'Название товара в сообщении отличается от названия добавленного'
        item_sum = self.browser.find_element(*ProductPageLocators.ITEM_SUM).text
        basket_sum = self.browser.find_element(*ProductPageLocators.BASKET_SUM).text
        assert item_sum == basket_sum, 'Стоимость корзины не совпадает с ценой товара'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "should have disappeared, but it didn't"
