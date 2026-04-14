'''
Dynamic xpath ->
//button[text()='START' Or text()='STOP']
//button[@name='start' or @name='stop']
//button[contains(@name,'st']
//button[starts-with(@name,'st')]

playwright locators ->
page.get_by_role("button",name=re.compile(r'ST.*'))

'''



import pytest
from playwright.sync_api import Page, expect

def test_xpath_locator(page:Page):
    url=page.goto("https://demowebshop.tricentis.com/")
    print ("this is a url: ",url)

    # # 1) Absolute xpath
    # logo=page.locator("//html[1]/body[1]/div[4]/div[1]/div[1]/div[1]/a[1]/img[1]")
    # expect(logo).to_be_visible()
    # page.wait_for_timeout(2000)

    # 2) Relative xpath  : tagname[@attribute='value']
    logo=page.locator("//img[@alt='Tricentis Demo Web Shop']")
    expect(logo).to_be_visible()
    page.wait_for_timeout(2000)

    # 3) xpath with contains
    product=page.locator("//h2/a[contains(@href,'computer')]")
    product_count=product.count()
    print("total products: ",product_count)

    print("first computer product : ", product.first.text_content())
    print("last computer product : ", product.last.text_content())
    print("nth computer product : ", product.nth(2).text_content())

    print("All products text : ", product.all_text_contents())

    print("printing products titles in looping statement : ")
    list_product_text= product.all_text_contents()
    for i in list_product_text:
        print(i)