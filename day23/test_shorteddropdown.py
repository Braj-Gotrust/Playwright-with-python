import pytest
from playwright.sync_api import sync_playwright, Page, expect


def test_multi_selector_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    #dropdown_options = page.locator("#colors>option")  # this is not sorted
    dropdown_options = page.locator("#animals>option")  # this is sorted

    text_options = [text.strip() for text in dropdown_options.all_text_contents()]

    original_list=text_options.copy()
    sorted_list=sorted(text_options)
    print("original list : ",original_list)
    print("shorted list : ",sorted_list)

    if original_list==sorted_list:
        print("Dropdown options are sorted order ")
    else:
        print("Dropdown options are not sorted order ")

    page.wait_for_timeout(2000)

