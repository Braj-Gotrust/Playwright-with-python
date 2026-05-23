import pytest
from playwright.sync_api import sync_playwright,Page,expect

@pytest.mark.skip
def test_mouse_hover(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    pointme=page.locator(".dropbtn")
    pointme.hover()
    laptop=page.locator(".dropdown-content a").nth(1)
       # OR
    #laptop=page.locator(".dropdown-content a:nth-child(2)")
    laptop.hover()
    page.wait_for_timeout(3000)

def test_mouse_rightclick(page: Page):
    page.goto("https://swisnl.github.io/jQuery-contextMenu/demo.html")
    button=page.locator(".context-menu-one ")
    #button.click() # this is by default left click
    button.click(button="right")  # this is right click

    # this is duble click
    #button.dblclick()  # this is a double click action

    page.wait_for_timeout(3000)






