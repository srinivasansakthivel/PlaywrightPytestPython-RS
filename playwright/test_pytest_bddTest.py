import pytest
from pytest_bdd import given, when, then, parsers, scenarios

from pageObjects.loginPage import LoginPage
from utils.apiBaseFramework import APIUtils


scenarios('/Users/srinivasansakthivel/PycharmProjects/PlaywrightPytestPython-RS/playwright/features/orderTransactions.feature')

@pytest.fixture
def shared_data():
    return {}

@given(parsers.parse('place the item with {username} and {password}'))
def place_item_order(playwright, username, password, shared_data):
    user_credentials = {'userEmail': username, 'userPassword': password}
    api_utils = APIUtils()
    order_id = api_utils.createOrder(playwright, user_credentials)
    shared_data['order_id'] = order_id

@given('the user is on the landing page')
def user_on_landing_page(browserInstance, shared_data):
    loginPage = LoginPage(browserInstance)
    loginPage.navigate_to_dashboard()
    shared_data['login_page'] = loginPage


@when(parsers.parse('I login to portal with {username} and {password}'))
def login_to_portal(username, password, shared_data):
    user_credentials = {'userEmail': username, 'userPassword': password}
    loginPage = shared_data['login_page']
    dashboardPage = loginPage.login(user_credentials['userEmail'], user_credentials['userPassword'])
    shared_data['dashboard_page'] = dashboardPage

@when('navigate to the order page')
def navigate_to_order_page(shared_data):
    dashboardPage = shared_data['dashboard_page']
    orderHistoryPage = dashboardPage.navigate_to_orders_from_dashboard()
    shared_data['order_history_page'] = orderHistoryPage


@when('select the orderId')
def select_order_id(shared_data):
    orderHistoryPage = shared_data['order_history_page']
    order_id = shared_data['order_id']
    orderDetailsPage = orderHistoryPage.selecting_order_id(order_id)
    shared_data['order_details_page'] = orderDetailsPage


@then('order message is successfully displayed')
def order_message_successfully_displayed(shared_data):
    orderDetailsPage = shared_data['order_details_page']
    order_id = shared_data['order_id']
    orderDetailsPage.validating_order_details_screen_message_and_order_id(order_id)