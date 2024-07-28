# Automation from Scratch
import pytest
import allure
import requests

url = "https://restful-booker.herokuapp.com"


@allure.title("End to End Scenario CRUD")
@allure.description("TC 1 - To verify Create booking")
@pytest.mark.crud
def test_create_booking_positive():
    # TO make Request in Restful booker
    # URL
    # Method - POST
    # Header - Content-Type - application/json
    # Body - Payload / Data - Dict / Json
    # Auth(No)
    base_url = "https://restful-booker.herokuapp.com"
    URL = base_url + "/booking"
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Choco",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2013-02-23",
            "checkout": "2014-10-23"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 200  # "to check status is 200 or not"

    # Response Body Verification
    # Headers
    # Status Code
    # JSON Schema Validation
    # Time Response
    response_data = response.json()
    assert response_data["bookingid"] is not None
    print(response_data["bookingid"])
    assert response_data["bookingid"] > 0
    assert type(response_data["bookingid"]) == int
    firstname = response_data["booking"]["firstname"]
    assert firstname == "Choco"
    