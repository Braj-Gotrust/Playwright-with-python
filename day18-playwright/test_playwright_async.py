# pre-requisite for Asynchrouns execution :-
# install pytest-asyncio plugin command :- pip install pytest-asyncio

from playwright.async_api import async_playwright,Page,expect
import pytest

@pytest.mark.asyncio
async def test_verifyPageUrl():
    async with async_playwright() as page:
        browser = await page.chromium.launch()
        mypage = await browser.new_page()
        await mypage.goto("https://playwright.dev/")
        await expect(mypage).to_have_url("https://playwright.dev/")   # expected url
