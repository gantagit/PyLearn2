# Automation from Scratch
import pytest
import allure
import requests

url = "https://restful-booker.herokuapp.com/booking"


@allure.title("Test GET request - Restful Booker Project#1")
@allure.description("TC#1 - This test case is to verify booking with a valid booking ID")
@allure.tag("p0", "smoke", "regression")
@allure.label("owner", "Vijay")
@allure.testcase("TC-1")
@pytest.mark.smoke
def test_verify_get_booking_by_valid_id1():
    response_data = requests.get(f"{url}/1")  # def get(url, params=None, **kwargs)
    print(response_data.json())
    print(response_data)
    assert response_data.status_code == 200


@allure.title("Test GET request - Restful Booker Project#1")
@allure.description("TC#2 - Negative Scenario to test status code of Valid Booking Id")
@pytest.mark.smoke
def test_verify_get_booking_by_valid_id2():
    response_data = requests.get(f"{url}/1")  # def get(url, params=None, **kwargs)
    print(response_data.json())
    print(response_data)
    assert response_data.status_code == 404


@allure.title("Test GET request - Restful Booker Project#1")
@allure.description("TC#3 - This test case is to verify booking with a valid booking ID")
@pytest.mark.smoke
def test_verify_get_booking_by_invalid_id():
    response_data = requests.get(f"{url}/$$$1234")  # def get(url, params=None, **kwargs)
    print(response_data.text)
    print(response_data)
    assert response_data.status_code == 404


@allure.title("Test GET request - Restful Booker Project#1")
@allure.description("TC#4 - Negative Scenario to test status code of InValid Booking Id")
@pytest.mark.smoke
def test_verify_get_booking_by_invalid_id2():
    response_data = requests.get(f"{url}/$$$1234")  # def get(url, params=None, **kwargs)
    print(response_data.text)
    print(response_data)
    assert response_data.status_code == 200


@allure.title("Test GET request - Restful Booker Project#1")
@allure.description("TC#5 - Get all booking id's")
@pytest.mark.smoke
def test_verify_get_all_bookings():
    response_data = requests.get(url)
    print(response_data.json())
    assert response_data.status_code == 200


@allure.title("Test GET request - Restful Booker Project#1")
@allure.description("TC#6 - Get all booking id's")
@pytest.mark.smoke
def test_verify_get_all_bookings2():
    response_data = requests.get(url)
    assert response_data.status_code != 200
