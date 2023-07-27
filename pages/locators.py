from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group > .btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner>p>a")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_REGISTRATION_INPUT = (By.ID, 'id_registration-email')
    PASSWORD_REGISTRATION_INPUT = (By.ID, 'id_registration-password1')
    PASSWORD_REGISTRATION_INPUT_TWICE = (By.ID, 'id_registration-password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '.register_form .btn-lg')


class ProductPageLocators:
    ADD_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, ".product_main h1")
    ITEM_NAME_IN_BASKET = (By.XPATH, "//div[@id='messages']/div[1]//strong")
    ITEM_SUM = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_SUM = (By.XPATH, "//div[@id='messages']/div[3]//strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert.alert-safe")
