import time

from playwright.sync_api import Page, expect, Playwright


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")


def test_playwrightShortCut(page:Page):
    page.goto("https://rahulshettyacademy.com")
    time.sleep(2)


def test_coreVariables(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning123")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    # Incorrect error message - Incorrect username/password.
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(3)


def test_Firefoxbrowser(playwright: Playwright):
    firefox_browser = playwright.firefox.launch(headless=False)
    page = firefox_browser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning123")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    # Incorrect error message - Incorrect username/password.
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(3)








