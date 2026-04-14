from playwright.sync_api import sync_playwright, Page, expect

def test_statictable(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    # locating table
    table=page.locator("table[name='BookTable'] tbody")
    expect(table).to_be_visible()
    #count all rows in the table
    rows = table.locator("tr")
        # OR
    #rows = page.locator("table[name='BookTable'] tbody tr")
    expect(rows).to_have_count(7)

    rows_count=rows.count()
    print("\nTotal number of row count : ",rows_count)
    #count all column in the table
    column=rows.locator("th")
       # OR
    #column= page.locator("table[name='BookTable'] tbody tr th")
    expect(column).to_have_count(4)

    column_count=column.count()
    print("\nTotal number of column count : ",column_count)

    #count second row data in the table
    second_rows_cell= rows.nth(1).locator("td")
    count1=second_rows_cell.count()
    print("\nSecond row cell count : ",count1)
    second_rows_text= second_rows_cell.all_inner_texts()
    print("\nTotal second row data : ",second_rows_text)
    expect(second_rows_cell).to_have_text(['Learn Selenium', 'Amit', 'Selenium', '300'])
    print("\nprinting second row data by for loop")
    for text in second_rows_text:
        print(text)

    # Read all the data from the table (Excluding header)
    all_rows_data=rows.all()
    for row in all_rows_data[1:]:  # Header is no including, start from index 1
        cols=row.locator("td").all_inner_texts()
        print(cols)

    # print book name and author name
    print("\nPrinting books name written by the 'Mukesh'")
    for row in all_rows_data[1:]:
        author_name = row.locator("td").nth(1).inner_text()
        if author_name == "Mukesh":
            book_name = row.locator("td").nth(0).inner_text()
            print(f"{book_name} \t {author_name}")

    print("\n Calculate total price of the books ")
    total_price = 0
    for row in all_rows_data[1:]:  # Header is no including, start from index 1
        price = row.locator("td").nth(3).inner_text()
        total_price += int(price)
    print("\nTotal price : ", total_price)






