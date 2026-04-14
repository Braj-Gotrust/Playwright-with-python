import pytest
from playwright.sync_api import sync_playwright, Page, expect

def test_single_selector_dropdown(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    # There are three way to select option from dropdown

    #page.locator("#country").select_option("India")  # get by label
    # OR
    page.locator("#country").select_option(label="India")  # get by label
    page.wait_for_timeout(1000)

    page.locator("#country").select_option(value="germany")  # get by value
    page.wait_for_timeout(1000)

    page.locator("#country").select_option(index=2)  # get by index
    page.wait_for_timeout(1000)

    dropdown_options=page.locator("#country>option")
    expect(dropdown_options).to_have_count(10)

    text_options=dropdown_options.all_text_contents()
    txt=[option.strip() for option in text_options]
    print(txt)

    #
    # txt=[text.strip() for text in dropdown_options.all_text_contents()]  # getting by list
    # print(txt)

    # print countries using loop
    for option in txt:
        print(option)

    page.wait_for_timeout(1000)

