from Pages.BasePage import BasePage


class ItemDetailsPage(BasePage):
    """Item Details Page Elements"""
    HEADER = ("xpath", "//*[@class='title']")
    BACK_TO_PRODUCTS_BTN = ("xpath", "//button[@id='back-to-products']")

    ITEM_DESC = ("xpath", "//*[@class='inventory_details_desc large_size']")
    ITEM_PRICE = ("xpath", "//*[@class='inventory_details_price']")

    ADD_TO_CART_BTN = ("id", "add-to-cart-sauce-labs-backpack")
    REMOVE_BTN = ("id", "remove-sauce-labs-backpack")

    """Constructor of Page Class"""

    def __init__(self, driver):
        super().__init__(driver)

    def get_details_page_title(self, title):
        return self.get_page_title(title)

    def get_item_description(self):
        if self.is_element_visible(self.ITEM_DESC):
            return self.get_element_text(self.ITEM_DESC)

    def get_item_price(self):
        if self.is_element_visible(self.ITEM_PRICE):
            return self.get_element_text(self.ITEM_PRICE)

    def click_add_to_cart_button(self):
        self.click_element(self.ADD_TO_CART_BTN)

    def is_remove_button_visible(self):
        return self.is_element_visible(self.REMOVE_BTN)

