# Test : create booking (post request with static body)
# request type : post
# data:  external json file
import json

from playwright.sync_api import Playwright

def test_create_booking(playwright:Playwright):
    base_url = "https://restful-booker.herokuapp.com"

    request_context = playwright.request.new_context()

    # load the data from the external file
    file = open("testdata/post_request_body.json", "r")
    request_body = json.load(file)

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
    assert booking["firstname"] == "Jim"
    assert booking["lastname"] == "Brown"
    assert booking["totalprice"] == 111
    assert booking["depositpaid"] == True
    assert booking["additionalneeds"] == "Breakfast"
    # nested json data validation
    assert booking["bookingdates"]["checkin"] == "2018-01-01"
    assert booking["bookingdates"]["checkout"] == "2019-01-01"

    # close the api context
    request_context.dispose()






