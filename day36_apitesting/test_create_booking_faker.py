# Test : create booking (post request with static body)
# request type : post
# data:  faker dynamic data


from datetime import timedelta, datetime
from faker import Faker
from playwright.sync_api import Playwright

def test_create_booking(playwright:Playwright):
    base_url = "https://restful-booker.herokuapp.com"

    request_context = playwright.request.new_context()

    # Faker dynamic data
    faker = Faker()
    first_name = faker.first_name()
    last_name = faker.last_name()
    total_price = faker.random_int(100, 10000)
    deposit_paid = faker.boolean()
    additional_needs = faker.word()
    checkin_date = datetime.now().strftime("%Y-%m-%d")
    checkout_date = (datetime.now() + timedelta(days=5)).strftime("%Y-%m-%d")

    request_body = {
        "firstname": first_name,
        "lastname": last_name,
        "totalprice": total_price,
        "depositpaid": deposit_paid,
        "bookingdates": {
            "checkin":  checkin_date,
            "checkout": checkout_date
        },
        "additionalneeds": additional_needs
    }

    response = request_context.post(f"{base_url}/booking", data = request_body)

    # validation
    assert response.ok
    assert response.status == 200
    response_body = response.json()
    print("\n Response Body : ",response_body)

    # field or attribute validation
    assert "bookingid" in response_body   # booking id present or not
    assert "booking" in response_body

    # data validation
    booking = response_body["booking"]
    assert booking["firstname"] == first_name
    assert booking["lastname"] == last_name
    assert booking["totalprice"] == total_price
    assert booking["depositpaid"] == deposit_paid
    assert booking["additionalneeds"] == additional_needs
    # nested json data validation
    assert booking["bookingdates"]["checkin"] == checkin_date
    assert booking["bookingdates"]["checkout"] == checkout_date

    # close the api context
    request_context.dispose()






