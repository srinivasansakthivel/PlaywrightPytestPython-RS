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

    def getToken(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post(url="/api/ecom/auth/login",
                                            data={"userEmail": "starsrini5@gmail.com", "userPassword": "Qwerty#1234"},)
        assert response.ok
        # print(response.json())
        responseBody = response.json()
        return responseBody["token"]

    def createOrder(self, playwright: Playwright):
        token = self.getToken(playwright)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post(url="/api/ecom/order/create-order",
                                            data=orderPayLoad,
                                            headers={"Authorization": token, "Content-Type": "application/json"})
        # print(response.json())
        response_body = response.json()
        orderId = response_body["orders"][0]
        return orderId
