# 1. Get the Response
# 2. Create the JSON schema - https://www.jsonschema.net/
# 3. Save that schema into the name.json file
# 4. If you want to validate the json schema - https://www.jsonschemavalidator.net/
# we import json schema
import json

from jsonschema import validate
from jsonschema.exceptions import ValidationError
import pytest
import allure

from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
# from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Util
import os

class TestCreateBookingJSONSchema(object):

    def load_schema(self,file_name):
        with open(file_name, 'r') as file:
            return json.load(file)
    @pytest.mark.positive
    @allure.title("Verify that Create Booking Status and Booking ID shouldn't be null")
    @allure.description(
        "Creating a Booking from the payload and verify that booking id should not be null and status code should be "
        "200 for the correct payload")
    def test_create_booking_schema(self):
        # URL, Payload, #headers
        response = post_requests(url=APIConstants.url_create_booking(),
                                 auth=None,
                                 headers=Util().common_headers_json(),
                                 payload=payload_create_booking(),
                                 in_json=False)

        booking_id = response.json()["bookingid"]
        verify_http_status_code(response_data=response, expect_data=200)
        verify_json_key_for_not_null(booking_id)

        # response with schema.json stored
        file_path = os.getcwd()+"/create_booking_schema.json"
        schema = self.load_schema(file_name=file_path)

        try:
            validate(instance=response.json(),schema=schema)
        except ValidationError as e:
            print(e.message)
            pytest.fail("Failed: JSON schema Error")
