from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def empty_shopping_list(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Присутствует список покупок, хотя не должен быть"

    def not_empty_shopping_text(self):
        assert self.is_not_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), \
            "Присутствует текст, что корзина пуста, хотя не должен быть"

    def empty_shopping_list_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), \
            "Отсутствует текст, что корзина пуста"


