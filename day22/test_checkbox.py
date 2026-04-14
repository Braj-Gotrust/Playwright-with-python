import pytest
from playwright.sync_api import Page, expect

def test_checkbox(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    sunday_checkbox=page.get_by_label("Sunday")
    sunday_checkbox.check()
    expect(sunday_checkbox).to_be_checked()
    page.wait_for_timeout(2000)


# count number of check box
    days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    checkboxs=[]
    for day in days:
        checkbox=page.get_by_label(day)
        checkboxs.append(checkbox)
    print("\nTotal number of check boxs : ",len(checkboxs))
    # OR
    # checkboxs=[page.get_by_label(day) for day in days]
    # print("\nTotal number of check boxs : ",len(checkboxs))

    # select all the checkboxes and assert each check box is selected
    for checkbox in checkboxs:
        checkbox.check()
        expect(checkbox).to_be_checked()
    page.wait_for_timeout(2000)

    # last 2 checkbox unselect/uncheck
    for checkbox in checkboxs[-2:]:
        checkbox.uncheck()
        expect(checkbox).not_to_be_checked()
    page.wait_for_timeout(2000)

    # Toggle checkboxes -> opposite- To checked checkbox will be uncheck and uncheck checkboxes will be checked, that is called toggle
    for checkbox in checkboxs:
        if checkbox.is_checked():
            checkbox.uncheck()
            expect(checkbox).not_to_be_checked()
        else:
            checkbox.check()
            expect(checkbox).to_be_checked()
    page.wait_for_timeout(2000)

    # Randomly select checkboxes
    indexes=[1,3]
    for i in indexes:
        checkboxs[i].check()
        expect(checkboxs[i]).to_be_checked()

    page.wait_for_timeout(2000)



