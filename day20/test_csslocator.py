'''
syntax :
tag id -> tag#id
tag class -> tag.class
tag attribute -> tag[attribute=value]
tag class attribute -> tag.class[attribute=value]
'''


import pytest
from playwright.sync_api import Page, expect

def test_verify_cc_locator(page: Page):
    page.goto("https://demowebshop.tricentis.com/")
    # tag#id
    page.locator("input#small-searchterms").fill("T-Shirts") # tag name is optional
    page.locator("#small-searchterms").fill("T-Shirts")
    page.wait_for_timeout(2000)

    
