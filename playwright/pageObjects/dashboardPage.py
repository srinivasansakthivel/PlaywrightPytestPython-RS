from .ordersHistoryPage import OrdersHistoryPage


class DashboardPage:
    def __init__(self, page):
        self.page = page


    def navigate_to_orders_from_dashboard(self):
        self.page.get_by_role("button", name="ORDERS").click()
        orderHistoryPage = OrdersHistoryPage(self.page)
        return orderHistoryPage
