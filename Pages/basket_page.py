from Pages.base_page import BasePage
from Pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        self.empty_basket_message_displayed()
        self.no_products_in_basket()

    def empty_basket_message_displayed(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "'Your basket is empty' message is not displayed"

    def no_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket is not empty"
