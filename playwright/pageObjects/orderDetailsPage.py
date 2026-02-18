from playwright.sync_api import expect


class OrderDetailsPage:

    def __init__(self, page):
        self.page = page

    def validating_order_details_screen_message_and_order_id(self, orderId):
        expect(self.page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
        assert self.page.locator('.col-text.-main').text_content() == orderId