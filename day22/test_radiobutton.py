import pytest
from playwright.sync_api import Page, expect

def test_radiobutton(page:Page ):
    page.goto("https://testautomationpractice.blogspot.com/")

    male_radio = page.locator("#male")

    # check the visibility of the element and enabled or not
    expect(male_radio).to_be_visible()
    expect(male_radio).to_be_enabled()



    # # male radio box should be checked
    # expect(male_radio).to_be_checked()

    # male radio button should not be checked
    expect(male_radio).not_to_be_checked()

    # select/check radio button
    male_radio.check()

    # male radio box should be checked
    expect(male_radio).to_be_checked()
    page.wait_for_timeout(2000)

    # select/check radio button
    female_radio=page.locator("#female")
    female_radio.check()

    # female radio box should be checked
    expect(female_radio).to_be_checked()




