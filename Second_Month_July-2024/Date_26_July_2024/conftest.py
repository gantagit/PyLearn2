# Fixture - Concept of python
import pytest
import requests
from dotenv import load_dotenv
import os

# global variables
base_url = str(os.getenv("URL"))
headers = {
    "Content-Type": "application/json"
}
auth_endpoint = base_url + "/auth"
auth_payload = {
    "username": os.getenv("username"),
    "password": os.getenv("password")
}
booking_endpoint = base_url + "/booking"
booking_payload = {
    "firstname": "VJ",
    "lastname": "Brown",
    "totalprice": 111,
    "depositpaid": False,
    "bookingdates": {
        "checkin": "2013-02-23",
        "checkout": "2014-10-23"
    },
    "additionalneeds": "Breakfast"
}


# fixtures
@pytest.fixture
def create_token():
    response = requests.post(url=auth_endpoint, headers=headers, json=auth_payload)
    assert response.status_code == 200
    token = response.json()["token"]
    print(token)
    return token


@pytest.fixture
def create_booking():
    response = requests.post(url=booking_endpoint, headers=headers, json=booking_payload)
    response_data = response.json()
    assert response.status_code == 200
    first_name = response_data["booking"]["firstname"]
    booking_id = response_data["bookingid"]
    assert first_name == "VJ"
    assert booking_id is not None
    assert isinstance(booking_id, int)  # assert type(booking_id) == int
    print(booking_id)
    return booking_id


@pytest.fixture
def launch_browser():
    return "Browser launched"


@pytest.fixture
def close_browser():
    return "Browser closed"
