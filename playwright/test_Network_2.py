from playwright.sync_api import Page, Playwright, expect
from pytest_playwright.pytest_playwright import browser

from utils.apiBase import APIUtils


def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=698aa34b48d62064b2f87f6b")


def test_network_2(page: Page):
    # Login to the website
    page.goto("https://rahulshettyacademy.com/client")
    # using customer id as * as it can accept any alphanumeric value
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.get_by_placeholder("email@example.com").fill("starsrini5@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Qwerty#1234")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    message = page.locator(".blink_me").text_content()
    print(message)


def test_session_storage(playwright: Playwright):
    apiUtils = APIUtils()
    getToken = apiUtils.getToken(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # script to inject the token into the session storage of the browser using jave scrip
    page.add_init_script(f"""localStorage.setItem('token', '{getToken}');""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text('Your Orders')).to_be_visible()




