from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import *
# from src.helpers.common_verification import verify_response_key_should_not_be_none, verify_http_status_code
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.utils.utils import Util

import allure
import pytest
import openpyxl


@pytest.fixture(scope="session")
def create_token():
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

    @pytest.fixture(scope="session")
    def get_booking_id():
        response = post_requests(url=APIConstants.url_create_booking(),
                                 auth=None,
                                 headers=Util().common_headers_json(),
                                 payload=payload_create_booking(),
                                 in_json=False)

        booking_id = response.json()["bookingid"]
        verify_http_status_code(response_data=response, expect_data=200)
        verify_json_key_for_not_null(booking_id)
        return booking_id

    @pytest.fixture(scope="session")
    def read_credentials_from_excel(file_path):
        credentials = []
        workbook = openpyxl.load_workbook(filename=file_path)
        sheet = workbook.active
        for row in sheet.iter_rows(min_row=2, values_only=True):
            username, password = row
            credentials.append(({
                "username": username,
                "password": password
            }))
        return credentials
    def create_auth_request(username, password):
        payload = {
        "username": username,
        "password": password
    }
    response = post_requests(
        url=APIConstants.url_create_token(),
        headers=Util().common_headers_json(),
        auth=None,
        payload=payload,
        in_json=False
    )
    return response