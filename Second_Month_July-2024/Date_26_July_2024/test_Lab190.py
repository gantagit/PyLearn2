# Automation from Scratch

# End to End Scenario of Restful booking

# Authentication - create token
# Create booking (Post
# Get booking (Get)
# Update booking (Put)
# Patch booking (Patch)
# Delete booking (Delete)

import allure
# import pytest
import requests
# import global_data




booking_endpoint = "https://restful-booker.herokuapp.com/booking"
update_payload = {
    "firstname": "VJ",
    "lastname": "GANT",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2013-02-23",
        "checkout": "2014-10-23"
    },
    "additionalneeds": ["Breakfast", "Lunch"]
}


@allure.title("TC #1 to update a Booking")
@allure.description("This test case is to update a Booking")
# @pytest.mark.crud
def test_update_booking(create_token, create_booking):
    update_endpoint = booking_endpoint + "/" + str(create_booking)
    update_headers = {
        "Content-Type": "application/json",
        "Cookie": "token=" + str(create_token)
    }
    response = requests.put(url=update_endpoint, headers=update_headers, json=update_payload)
    response_data = response.json()
    print(response.json())
    assert response.status_code == 200
    last_name = response_data["lastname"]
    deposit_paid = response_data["depositpaid"]
    additional_needs = response_data["additionalneeds"]
    assert last_name == "GANT"
    assert deposit_paid is True
    assert additional_needs == ["Breakfast", "Lunch"]
    print(last_name, deposit_paid, additional_needs)


@allure.title("TC #2 to delete a Booking")
@allure.description("This test case is to delete a Booking")
# @pytest.mark.crud
def test_delete_booking(create_token, create_booking):
    update_endpoint = booking_endpoint + "/" + str(create_booking)
    update_headers = {
        "Content-Type": "application/json",
        "Cookie": "token=" + str(create_token)
    }
    response = requests.delete(url=update_endpoint, headers=update_headers)
    # here i can use the same update endpoint and update headers for delete request
    # response_data = response.json()
    # print(response.json())
    assert response.status_code == 201
    print(response.text)
    # print(response_data)
