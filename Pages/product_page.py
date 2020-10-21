from selenium.common.exceptions import NoSuchElementException

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        base_page = BasePage(self.browser, self.browser.current_url)
        add_button.click()
        base_page.solve_quiz_and_get_code()

    def should_be_current_product_is_added_to_the_basket(self):
        self.should_be_product_name_in_alert()
        self.should_be_price_in_alert()

    def should_be_product_name_in_alert(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_alert = self.browser.find_element(*ProductPageLocators.SUCCESS_ALERT_PRODUCT_NAME).text
        assert product_name == product_name_in_alert, \
            f"Product name in alert is incorrect, expected '{product_name}', but was '{product_name_in_alert}'"

    def should_be_price_in_alert(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_in_alert = self.browser.find_element(*ProductPageLocators.INFO_ALERT_BASKET_TOTAL).text
        assert product_price == product_price_in_alert, \
            f"Expected product price in alert is '{product_price}', but was '{product_price_in_alert}'"
