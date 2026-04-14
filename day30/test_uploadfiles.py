import pytest
from playwright.sync_api import Playwright,Page,expect

@pytest.mark.skip
def test_upload_singlefile(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    # upload single file
    page.locator("#singleFileInput").set_input_files("uploads/Report.pdf")
    page.locator("button:has-text('Upload Single File')").click()

    # validation
    msg=page.locator("#singleFileStatus")
    expect(msg).to_contain_text("Report.pdf")
    print("file upload successfully ! ")
    page.wait_for_timeout(5000)


def test_upload_multiplefiles(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    # upload multiple files
    files=["uploads/Report.pdf","uploads/Login.txt"]
    page.wait_for_timeout(3000)
    page.locator("#multipleFilesInput").set_input_files(files)
    page.wait_for_timeout(3000)
    page.locator("button:has-text('Upload Multiple Files')").click()

    # validation
    msg=page.locator("#multipleFilesStatus")
    expect(msg).to_contain_text("Report.pdf")
    expect(msg).to_contain_text("Login.txt")
    page.wait_for_timeout(3000)

    print("Multiple file upload successfully ! ")
    page.wait_for_timeout(5000)