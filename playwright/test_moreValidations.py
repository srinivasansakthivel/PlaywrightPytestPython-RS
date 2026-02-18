import time

from playwright.sync_api import Page, expect


def test_UIChecks(page: Page):
    # Handling the hide and checking the visible of the text box using placeholder text
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    # Handling the alerts
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name="Confirm").click()
    time.sleep(5)

    #Handling - Mouse Hover
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()


    # Frame handling
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link", name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers!")

    # Check the price of the rice is 37 in the web table
    # identify the price column
    # identify the price row
    # extract the price of the rice
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            priceColValue = index
            print(f"Price Column value is {priceColValue}")
            break

    riceRow = page.locator("th").filter(has_text="Rice")
    expect(riceRow.locator("td").nth(priceColValue)).to_have_text("37")






