# Create Token
# Create Booking ID
# Update the Booking (PUT) - Booking ID, Token
# Delete the Booking

# Test cases Verify that created booking id when we update we are able to update it and delete it.
# Create Token
# Create Booking
# test_update() -> We need to pass the data to test update
# Fixtures -> can be basically help to pass the data in pytest

import allure
import pytest

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
# from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Util


class TestCRUDBooking(object):

    @pytest.fixture()
    def create_token(self):
        response = post_requests(
            url=APIConstants.url_create_token(),
            headers=Util().common_headers_json(),
            auth=None,
            payload=payload_create_token(),
            in_json=False
        )
        verify_http_status_code(response_data=response, expect_data=200)
        verify_json_key_for_not_null_token(response.json()["token"])
        return response.json()["token"]

    @pytest.fixture()
    def get_booking_id(self):
        response = post_requests(url=APIConstants.url_create_booking(),
                                 auth=None,
                                 headers=Util().common_headers_json(),
                                 payload=payload_create_booking(),
                                 in_json=False)

        booking_id = response.json()["bookingid"]
        verify_http_status_code(response_data=response, expect_data=200)
        verify_json_key_for_not_null(booking_id)
        return booking_id

    @allure.title("Test CRUD operation Update(PUT)")
    @allure.description(
        "Verify that Full Update with the booking ID and Token is working")
    def test_update_booking_id_token(self, create_token, get_booking_id):
        booking_id = get_booking_id
        token = create_token
        put_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        response = put_requests(
            url=put_url,
            headers=Util().common_headers_put_delete_patch_cookie(token=token),
            payload=payload_create_booking(),
            auth=None,
            in_json=False
        )
        verify_json_key_for_not_null(response.json()["firstname"])
        verify_response_key(response.json()["firstname"], expected_data="Satya")
        verify_json_key_for_not_null(response.json()["lastname"])
        verify_response_key(response.json()["lastname"], expected_data="Pedada")
        verify_http_status_code(response_data=response, expect_data=200)

    @allure.title("Test CRUD operation Update(delete)")
    @allure.description(
        "Verify booking gets deleted with the booking ID and Token.")
    def test_delete_booking_id(self, create_token, get_booking_id):
        booking_id = get_booking_id
        token = create_token
        delete_url = APIConstants.url_patch_put_delete(booking_id=booking_id)
        response = delete_requests(
            url=delete_url,
            headers=Util().common_headers_put_delete_patch_cookie(token=token),
            auth=None,
            in_json=False
        )
        verify_response_delete(response=response.text)
        verify_http_status_code(response_data=response, expect_data=201)


