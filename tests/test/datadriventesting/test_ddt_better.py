# Read the CSV or EXCEL file
# Create a Function create_tokenwhich can take values from the Excel File
# Verify the Excepted Result

# Read The Excel - openpyxl
import openpyxl
import pytest
import requests

from src.constants.api_constants import APIConstants
from src.utils.utils import Util
from src.helpers.api_requests_wrapper import *

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


@pytest.mark.parametrize("user_cred",read_credentials_from_excel("/Users/user/PycharmProjects/Py2xAPIAutomationFramework/pythonProject1/tests/test/datadriventesting/testdata_ddt_123.xlsx"))
def test_create_auth_with_excel(user_cred):
    username = user_cred["username"]
    password = user_cred["password"]
    print(username,password)
    response = create_auth_request(username=username, password=password)
    print(response.status_code)
