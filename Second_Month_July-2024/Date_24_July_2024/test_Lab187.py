# Automation from Scratch

# End to End Scenario of Restful booking

# Authentication - create token
# Create booking (Post
# Get booking (Get)
# Update booking (Put)
# Patch booking (Patch)
# Delete booking (Delete)


import pytest
import allure
import requests

base_url = "https://restful-booker.herokuapp.com"
auth_url = base_url + "/auth"
booking_url = base_url + "/booking"
headers = {
    "Content-Type": "application/json"
}
auth_payload = {
    "username": "admin",
    "password": "password123"
}

payload = {
    "firstname": "Vijay",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2013-02-23",
        "checkout": "2014-10-23"
    },
    "additionalneeds": "Breakfast"
}


def create_token():
    auth_response = requests.post(url=auth_url, headers=headers, json=auth_payload)
    auth_response_data = auth_response.json()
    token = auth_response_data["token"]
    print(token)
    return token


def create_booking():
    response = requests.post(url=booking_url, headers=headers, json=payload)
    response_data = response.json()
    booking_id = response_data["bookingid"]
    print(booking_id)
    return booking_id


@allure.title("TC#1 Update booking")
@allure.description("Test Case to verify Update booking")
@pytest.mark.crud
def test_update_booking():
    update_payload = {
        "firstname": "VJ",
        "lastname": "GANT",
        "totalprice": 111,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2013-02-23",
            "checkout": "2014-10-23"
        },
        "additionalneeds": "Breakfast"
    }
    put_url = booking_url + "/" + str(create_booking())
    update_headers = {
        "Content-Type": "application/json",
        "Cookie": "token=" + create_token()
    }
    response = requests.put(url=put_url, headers=update_headers, json=update_payload)
    response_data = response.json()
    assert response_data["firstname"] == "VJ"
    assert response_data["lastname"] == "GANT"
    assert response_data["depositpaid"] == False
