import pytest
from playwright.sync_api import sync_playwright, Page, expect

def test_multi_selector_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # There are three way to select option from dropdown
    #page.locator("#colors").select_option(["Red", "Green", "White"])  # get by label
    # OR
    #page.locator("#colors").select_option(label=["Red", "Green", "White"])  # get by label

    #page.locator("#colors").select_option(value=["red", "green", "white"])  # get by value

    #page.locator("#colors").select_option(index=[0, 2, 4])  # get by index

    dropdown_options= page.locator("#colors>option")
    expect(dropdown_options).to_have_count(7)

    




    page.wait_for_timeout(2000)

