import pytest
from playwright.sync_api import Playwright,Page,expect
import os

def test_download_file(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")
    page.locator("#inputText").fill("welcome")
    page.locator("#generateTxt").click()   # this will generate the link for download

    # # Approach 1 : register an event
    # def handle_download(download):
    #     download.save_as("downloads/textfile.txt")
    # page.on("download", handle_download)

    # # Approach 2 : using 'lambda' function
    page.on("download",lambda download: download.save_as("downloads/textfile.txt"))

    page.locator("#txtDownloadLink").click()  # this will download the file
    page.wait_for_timeout(5000)

    if os.path.exists("downloads/textfile.txt"):
        print("file exists")
    else:
        print("file not exists")


