from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_requests
# from src.helpers.common_verification import verify_http_status_code, verify_json_key_for_not_null
from src.helpers.common_verification import *
from src.helpers.payload_manager import payload_create_booking
from src.utils.utils import Util

import allure
import pytest

class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Verify that Create Booking Status and Booking ID shouldn't be null")
    @allure.description(
        "Creating a Booking from the payload and verify that booking id should not be null and status code should be "
        "200 for the correct payload")
    def test_create_booking_positive(self):
        # URL, Payload, #headers
        response = post_requests(url=APIConstants.url_create_booking(),
                                 auth=None,
                                 headers=Util().common_headers_json(),
                                 payload=payload_create_booking(),
                                 in_json=False)

        booking_id = response.json()["bookingid"]
        actual_status_code = response.status_code
        verify_http_status_code(response_data=response, expect_data=200)
        verify_json_key_for_not_null(booking_id)

    @pytest.mark.negative
    def test_create_booking_negative(self):
        # Url, Headers, Payload
        response = post_requests(url=APIConstants.url_create_booking(),auth=None,headers=Util().common_headers_json(),
                                 payload={},in_json=False)

        actual_status_code = response.status_code
        verify_http_status_code(response, expect_data=500)





