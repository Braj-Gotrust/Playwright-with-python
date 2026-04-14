import pytest
from playwright.sync_api import Page,expect

def test_inputbox(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #locate the element
    name=page.locator("#name")

    # check the visibility of the element and enabled or not
    expect(name).to_be_visible()
    expect(name).to_be_enabled()

    # check the element of the element
    expect(name).to_have_attribute("maxlength","15")

    # get the value of attribute
    len=name.get_attribute("maxlength")
    print("\nMaximum length of the input field : ",len)

    # fill the value of input field
    name.fill("braj")

    # get the value of input field
    getname=name.input_value()
    print("Get the value of the input field : ",getname)
    page.wait_for_timeout(2000)




