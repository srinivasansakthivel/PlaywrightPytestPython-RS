from playwright.sync_api import Playwright

orderPayLoad = {
    "orders": [
        {
            "country": "British Indian Ocean Territory",
            "productOrderedId": "6960eae1c941646b7a8b3ed3"
        }
    ]
}


class APIUtils:

    def getToken(self, playwright: Playwright, user_credentials):
        user_email = user_credentials['userEmail']
        user_password = user_credentials['userPassword']
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post(url="/api/ecom/auth/login",
                                            data={"userEmail": user_email, "userPassword": user_password},)
        assert response.ok
        # print(response.json())
        responseBody = response.json()
        return responseBody["token"]

    def createOrder(self, playwright: Playwright, user_credentials):
        token = self.getToken(playwright, user_credentials)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post(url="/api/ecom/order/create-order",
                                            data=orderPayLoad,
                                            headers={"Authorization": token, "Content-Type": "application/json"})
        # print(response.json())
        response_body = response.json()
        orderId = response_body["orders"][0]
        return orderId
