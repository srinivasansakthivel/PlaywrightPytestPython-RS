import pytest
from playwright.sync_api import Page

fakePayloadOrderResponse = {"data": [], "message": "No Orders"}


def intercept_response(route):
    route.fulfill(
        json=fakePayloadOrderResponse
    )


@pytest.mark.smoke
def test_network_1(page: Page):
    # Login to the website
    page.goto("https://rahulshettyacademy.com/client")
    # using customer id as * as it can accept any alphanumeric value
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("starsrini5@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Qwerty#1234")
    page.get_by_role("button", name="Login").click()

    # Navigate to the orders history and check for the order ID
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    order_text = page.locator(".mt-4").text_content()
    print(order_text)
