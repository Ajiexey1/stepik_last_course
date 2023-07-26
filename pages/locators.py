from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ITEM_NAME_IN_BASKET = (By.XPATH, "//div[@id='messages']/div[1]//strong")
    ITEM_SUM = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_SUM = (By.XPATH, "//div[@id='messages']/div[3]//strong")
