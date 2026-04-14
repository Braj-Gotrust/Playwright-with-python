from playwright.sync_api import sync_playwright,Page,expect





def test_jquery_datepicker(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    date_input=page.locator("#datepicker")
    is_future = True
    year="2028"
    month="March"
    date="25"
    date_input.click()
    select_date(page, year, month, date, is_future)
    print("selected date ======> : ",date_input.input_value())
    expect(date_input).to_have_value("03/25/2028")
    page.wait_for_timeout(5000)


def select_date(page, target_year, target_month, target_date, is_future):
    # selecting month and year from the date picker
    while True:
        current_month = page.locator(".ui-datepicker-month").text_content().strip()
        current_year = page.locator(".ui-datepicker-year").text_content().strip()

        if current_year == target_year and current_month == target_month:
            break
        if is_future == True:
            page.locator(".ui-datepicker-next").click() # for future date
        else:
            page.locator(".ui-datepicker-prev").click()  # for past date

    all_dates = page.locator(".ui-datepicker-calendar td").all()
    # selecting date from the date picker
    for date in all_dates:
        date_text = date.inner_text()
        if date_text == target_date:
            date.click()
            break