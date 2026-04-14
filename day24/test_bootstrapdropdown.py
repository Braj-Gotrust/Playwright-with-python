from os import wait

import pytest
from playwright.sync_api import Page,expect

def test_bootstrapdropdown(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.locator("input[name='username']").fill("admin")  # css Selectors
    page.locator("input[name='password']").fill("admin123")
    page.locator("button[type='submit']").click()
    page.wait_for_timeout(3000)

    # click on PIM
    page.get_by_text("PIM").click()  # playwright locator
    page.wait_for_timeout(3000)

    # click on the Job title dropdown
    page.locator("form i").nth(2).click()  # this will open options from the dropdown
    page.wait_for_timeout(3000)

    # page.get_by_text("Automaton Tester").click()
    # page.wait_for_timeout(3000)

    # page.locator("form i").nth(2).click()
    # page.get_by_text("Chief Executive Officer").click()
    # page.wait_for_timeout(3000)

    # Capture all the options of the dropdown
    dropdowns=page.locator("div[role='listbox'] span")
    count=dropdowns.count()
    print("\nTotal number of dropdown elements :",count)
    expect(dropdowns).to_have_count(count)
    page.wait_for_timeout(3000)
    print("\nAll dropdown element text list  :",dropdowns.all_text_contents())

    # print dropdowns element one by one using loop stetment
    for i in range(count):
        txt=dropdowns.nth(i).text_content()
        print(txt)

    for i in range(count):
        text=dropdowns.nth(i).text_content()
        if text=="Automaton Tester":
            print("matching successfully : ")
            dropdowns.nth(i).click()
            break
    page.wait_for_timeout(3000)

