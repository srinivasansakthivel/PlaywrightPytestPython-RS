#
# import time
#
# from playwright.sync_api import Playwright, expect
#
#
# def test_sherlock(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://sherlock.qa.pointz.in/login")
#     page.get_by_role("button", name="Sign In With Google").click()
#     page.get_by_role("button", name="Continue with Google").click()
#     page.get_by_role("textbox", name="Email or phone").click()
#     page.get_by_role("textbox", name="Email or phone").fill("srinivasan@epifi.com")
#     time.sleep(2)
#     page.get_by_role("textbox", name="Email or phone").press("Enter")
#     time.sleep(3)
#     page.get_by_role("textbox", name="Enter your password").fill("Starcitizen9@")
#     time.sleep(3)
#     page.get_by_role("textbox", name="Enter your password").press("Enter")
#     time.sleep(15)
#     expect(page.get_by_text("STOCK_GUARDIAN_VKYC_CALL_AGENT")).to_be_visible()
#     expect(page.locator("#root")).to_contain_text("STOCK_GUARDIAN_VKYC_CALL_AGENT")
#     page.get_by_text("STOCK_GUARDIAN_VKYC_CALL_AGENT").click()
#     expect(page.get_by_role("heading")).to_contain_text("vkyc")
#     expect(page.locator("svg").first).to_be_visible()
#     expect(page.get_by_role("img", name="user-glyph").locator("path")).to_be_visible()
#     expect(page.locator("#root")).to_contain_text("srinivasan")
#     expect(page.locator("#root")).to_contain_text("Log Out")
#     expect(page.locator("#root")).to_contain_text("VKYC Flow")
#     expect(page.get_by_role("button", name="Back Arrow")).to_be_visible()
#
#     # ---------------------
#     context.close()
#     browser.close()
