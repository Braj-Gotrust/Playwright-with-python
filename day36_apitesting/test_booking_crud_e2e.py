"""
1) create booking (post) -> booking id
2) get booking details (get) -> by id, by name, by dates
3) create token (post/auth)
4) partial update booking (patch)
5) full update booking (put)
6) delete booking (delete)
"""
import json
import pytest
from playwright.sync_api import Playwright

# base url
base_url = "https://restful-booker.herokuapp.com"

# utility function -> read json file
def read_json(file_path):
        file = open(file_path,"r")
        data = json.load(file)
        return data

# fixture function - creates playwright request context
@pytest.fixture(scope="session")
def request_context(playwright:Playwright):
        context = playwright.request.new_context()
        yield context
        context.dispose()

# 1) create booking (post) -> booking id
def test_create_booking(request_context):
        data = read_json("testdata/post_request_body.json")   # data is a verible
        response = request_context.post(f"{base_url}/booking", data=data)   # data is a keyword
        assert response.ok, "post request failed"
        assert response.status == 200, "post request failed"

        response_body = response.json()
        print("\nCreate booking response : ",response_body)

        assert "bookingid" in response_body, "booking id not found in response"
        assert "booking" in response_body, "booking details not found in response"

        booking = response_body["booking"]

        booking["firstname"] = data["firstname"]
        booking["lastname"] = data["lastname"]
        booking["totalprice"] = data["totalprice"]
        booking["depositpaid"] = data["depositpaid"]
        booking["bookingdates"]["checkin"] = data["bookingdates"]["checkin"]
        booking["bookingdates"]["checkout"] = data["bookingdates"]["checkout"]
        booking["additionalneeds"] = data["additionalneeds"]

        # we are making booking_id is the global to access in other test method
        global booking_id
        booking_id = response_body["bookingid"]
        global check_in
        check_in = booking["bookingdates"]["checkin"]
        global check_out
        check_out = booking["bookingdates"]["checkout"]




# 2) get booking details (get) -> by id
def test_get__booking_by_id(request_context):
        response = request_context.get(f"{base_url}/booking/{booking_id}")   # https://restful-booker.herokuapp.com/booking/1

        assert response.ok, "post request failed"
        assert response.status == 200, "post request failed"

        response_body = response.json()
        print(f"\nBooking details fetched by id {booking_id} : ",response_body)

        assert "firstname" in response_body, "first name is not found in response"
        assert "lastname" in response_body, "lastname is not found in response"



# 2) get booking details (get) -> by name
def test_get__booking_by_name(request_context):
        names_params = {"firstname":"Sally", "lastname":"Brown"}

        # passing query parameters
        # https://restful-booker.herokuapp.com/booking?firstname=sally&lastname=brown
        response = request_context.get(f"{base_url}/booking/", params=names_params)

        assert response.ok, "post request failed"
        assert response.status == 200, "post request failed"

        response_body = response.json()
        print(f"\nBooking ID's fetched by name {names_params} : ",response_body)

        # assert len(response_body)>0
        # for item in response_body:
        #         assert "bookingid" in item, "booking id not found in response"


# 2) get booking details (get) -> by date
def test_get__booking_by_date(request_context):
        dates_params = {"checkin": check_in, "checkout": check_out}

        # passing query parameters
        # https://restful-booker.herokuapp.com/booking?checkin=2014-03-13&checkout=2014-05-21
        response = request_context.get(f"{base_url}/booking/", params=dates_params)

        assert response.ok, "post request failed"
        assert response.status == 200, "post request failed"

        response_body = response.json()
        print(f"\nBooking ID's fetched by date {dates_params} : ", response_body)

        # for item in response_body:
        #         assert "bookingid" in item, "booking id not found in response"


# 3) create token (post/auth)
def test_create_token(request_context):
        data = read_json("testdata/token_request_body.json")
        response = request_context.post(f"{base_url}/auth/", data=data)   # https://restful-booker.herokuapp.com/auth

        assert response.ok, "post request failed"
        assert response.status == 200, "post request failed"

        response_body = response.json()
        print(f"\nToken creation response : ",response_body)

        global token
        token = response_body["token"]

        assert len(token) > 5, "token should not be empty"



# 4) partial update booking (patch)
def test_partial_update_booking(request_context):
        data = read_json("testdata/patch_request_body.json")
        response = request_context.patch(f"{base_url}/booking/{booking_id}", data=data, headers={"Cookie": f"token={token}" })

        assert response.ok, "patch request failed"
        assert response.status == 200, "patch request failed"

        response_body = response.json()
        print(f"\nPartial update response for booking id {booking_id} : ",response_body)

        for key in data.keys():
                assert key in response_body, "partial update response not found in response"
                assert response_body[key] == data[key], "partial update response not found in response"




# 5) full update booking (put)
def test_full_update_booking(request_context):
        data = read_json("testdata/put_request_body.json")
        response = request_context.put(f"{base_url}/booking/{booking_id}", data=data, headers={"Cookie": f"token={token}" })

        assert response.ok, "put request failed"
        assert response.status == 200, "put request failed"

        response_body = response.json()
        print(f"\nfull update response for booking id {booking_id} : ",response_body)

        # assertion with loop statement
        for key in data.keys():
                assert key in response_body, "partial update response not found in response"
                assert response_body[key] == data[key], "partial update response not found in response"

        # assertion with individual key and value
        assert response_body["firstname"] == data["firstname"], "partial update response not found in response"
        assert response_body["lastname"] == data["lastname"], "partial update response not found in response"
        assert response_body["totalprice"] == data["totalprice"], "partial update response not found in response"




# 6) delete booking (delete)
def test_delete_booking(request_context):
        response = request_context.delete(f"{base_url}/booking/{booking_id}", headers={"Cookie": f"token={token}" })

        assert response.status == 201, "delete request failed"

        print("\nBooking delete successfully ==>id :", booking_id)




