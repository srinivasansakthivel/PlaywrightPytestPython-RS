import json

import pytest
from playwright.sync_api import Playwright, expect

from conftest import user_credentials
from pageObjects.loginPage import LoginPage
from conftest import browserInstance

from utils.apiBaseFramework import APIUtils

# JSON file > utils > access test dat into this test case
with open('/Users/srinivasansakthivel/PycharmProjects/PlaywrightPytestPython-RS/playwright/data/credentials.json') as f:
    test_data = json.load(f)
    print(test_data)
    user_credentials_list = test_data['user_credentials']

@pytest.mark.smoke
@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_web_api(playwright: Playwright, browserInstance, user_credentials):
    #Getting the credentials from the user_credentials fixture
    userEmail = user_credentials['userEmail']
    userPassword = user_credentials['userPassword']

    # create order > orderID using API
    api_utils = APIUtils()
    order_id = api_utils.createOrder(playwright, user_credentials)

    # Login to the website
    loginPage = LoginPage(browserInstance)
    loginPage.navigate_to_dashboard()
    dashboardPage = loginPage.login(userEmail, userPassword)

    # Navigate to the orders history and check for the order ID
    orderHistoryPage = dashboardPage.navigate_to_orders_from_dashboard()

    # Navigating to the order history page
    orderDetailsPage = orderHistoryPage.selecting_order_id(order_id)
    orderDetailsPage.validating_order_details_screen_message_and_order_id(order_id)