# Fixture - Concept of python
import pytest


@pytest.fixture
def create_token():
    abc = 4
    return abc


@pytest.fixture
def create_booking_id():
    booking_id = 123
    return booking_id


def test_update_booking_id(create_token, create_booking_id):
    print("Token = " + str(create_token))
    print("Booking_Id = ", int(create_booking_id))
    sum = 4 + int(create_booking_id)
    print("Sum = ", sum)
