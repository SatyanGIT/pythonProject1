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
import logging

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
# from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Util


class TestCRUDBooking(object):

    @allure.title("Test CRUD operation Update(PUT)")
    @allure.description(
        "Verify that Full Update with the booking ID and Token is working")
    def test_update_booking_id_token(self, create_token, get_booking_id):
        logging.basicConfig(level=logging.INFO)
        logger = logging.getLogger(__name__)
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
        logger.info("Request is made"+ str(response))
        verify_json_key_for_not_null(response.json()["firstname"])
        verify_response_key(response.json()["firstname"], expected_data="Satya")
        verify_json_key_for_not_null(response.json()["lastname"])
        verify_response_key(response.json()["lastname"], expected_data="Pedada")
        verify_http_status_code(response_data=response, expect_data=200)
        logger.info("request status code" + str(response.status_code))

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


