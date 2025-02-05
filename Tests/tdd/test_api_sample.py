import pytest
import allure
import os
import importlib.util

# Path to the commonAPISteps.py
common_api_steps_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../apiAutomation/commonAPISteps.py'))

# Load the module
spec = importlib.util.spec_from_file_location("commonAPISteps", common_api_steps_path)
commonAPISteps = importlib.util.module_from_spec(spec)
spec.loader.exec_module(commonAPISteps)

# Fixture for setting up and tearing down the base URL
@pytest.fixture(scope="module")
def base_url():
    return "https://reqres.in/api"

@allure.feature('API Tests')
@allure.story('Demo Test')
def test_api_demo(base_url):

    # Test GET List of Users
    with allure.step("GET List of Users"):
        response = commonAPISteps.CommonApiSteps.send_get_request(f"{base_url}/users?page=2")
        commonAPISteps.CommonApiSteps.check_status_code(response, 200)
        commonAPISteps.CommonApiSteps.validate_response_contains_key(response, 'data')
        allure.attach(response.text, name="GET Response", attachment_type=allure.attachment_type.JSON)

    # Test POST Create a New User
    with allure.step("POST Create a New User"):
        user = {
            "name": "morpheus",
            "job": "leader"
        }
        response = commonAPISteps.CommonApiSteps.send_post_request(f"{base_url}/users", json=user)
        commonAPISteps.CommonApiSteps.check_status_code(response, 201)
        commonAPISteps.CommonApiSteps.validate_response_contains_key(response, 'id')
        commonAPISteps.CommonApiSteps.validate_response_contains_key(response, 'createdAt')
        assert response.json().get("name") == user["name"]
        assert response.json().get("job") == user["job"]
        allure.attach(response.text, name="POST Response", attachment_type=allure.attachment_type.JSON)

    # Test PUT Update a User
    with allure.step("PUT Update a User"):
        user = {
            "name": "morpheus",
            "job": "zion resident"
        }
        response = commonAPISteps.CommonApiSteps.send_put_request(f"{base_url}/users/2", json=user)
        commonAPISteps.CommonApiSteps.check_status_code(response, 200)
        commonAPISteps.CommonApiSteps.validate_response_contains_key(response, 'updatedAt')
        allure.attach(response.text, name="PUT Response", attachment_type=allure.attachment_type.JSON)

    # Test DELETE a User
    with allure.step("DELETE a User"):
        response = commonAPISteps.CommonApiSteps.send_delete_request(f"{base_url}/users/2")
        commonAPISteps.CommonApiSteps.check_status_code(response, 204)
        allure.attach(response.text, name="DELETE Response", attachment_type=allure.attachment_type.TEXT)
