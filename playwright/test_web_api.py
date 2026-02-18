from playwright.sync_api import Playwright, expect

from utils.apiBase import APIUtils


def test_e2e_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # create order > orderID using API
    api_utils = APIUtils()
    order_id = api_utils.createOrder(playwright)

    # Login to the website
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("starsrini5@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Qwerty#1234")
    page.get_by_role("button", name="Login").click()

    # Navigate to the orders history and check for the order ID
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()

    # Navigating to the order history page
    row = page.locator("tr").filter(has_text=order_id)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    assert page.locator('.col-text.-main').text_content() == order_id
    context.close()