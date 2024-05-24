import requests
import jsonschema

class CommonApiSteps:

    @staticmethod
    def send_get_request(url, headers=None, params=None):
        response = requests.get(url, headers=headers, params=params)
        return response

    @staticmethod
    def send_post_request(url, headers=None, data=None, json=None):
        response = requests.post(url, headers=headers, data=data, json=json)
        return response

    @staticmethod
    def send_put_request(url, headers=None, data=None, json=None):
        response = requests.put(url, headers=headers, data=data, json=json)
        return response

    @staticmethod
    def send_delete_request(url, headers=None, data=None):
        response = requests.delete(url, headers=headers, data=data)
        return response

    @staticmethod
    def send_patch_request(url, headers=None, data=None, json=None):
        response = requests.patch(url, headers=headers, data=data, json=json)
        return response

    @staticmethod
    def send_head_request(url, headers=None):
        response = requests.head(url, headers=headers)
        return response

    @staticmethod
    def send_options_request(url, headers=None):
        response = requests.options(url, headers=headers)
        return response

    @staticmethod
    def send_get_request_with_auth(url, token, headers=None):
        if headers is None:
            headers = {}
        headers['Authorization'] = f'Bearer {token}'
        response = requests.get(url, headers=headers)
        return response

    @staticmethod
    def send_post_request_with_auth(url, data=None, json=None, token=None, headers=None):
        if headers is None:
            headers = {}
        headers['Authorization'] = f'Bearer {token}'
        response = requests.post(url, headers=headers, data=data, json=json)
        return response

    @staticmethod
    def send_get_request_with_params(url, params=None, headers=None):
        response = requests.get(url, headers=headers, params=params)
        return response

    @staticmethod
    def check_status_code(response, expected_status):
        assert response.status_code == expected_status, f"Expected {expected_status}, got {response.status_code}"

    @staticmethod
    def check_response_json(response, expected_json):
        assert response.json() == expected_json, f"Expected {expected_json}, got {response.json()}"

    @staticmethod
    def check_response_headers(response, expected_headers):
        for key, value in expected_headers.items():
            assert response.headers.get(key) == value, f"Expected {key}: {value}, got {response.headers.get(key)}"

    @staticmethod
    def validate_json_schema(response, schema):
        jsonschema.validate(instance=response.json(), schema=schema)

    @staticmethod
    def validate_response_time(response, max_response_time):
        assert response.elapsed.total_seconds() * 1000 < max_response_time, f"Expected response time < {max_response_time}ms, got {response.elapsed.total_seconds() * 1000}ms"

    @staticmethod
    def validate_response_contains_key(response, key):
        assert key in response.json(), f"Expected key '{key}' in response, but it was not found"

    @staticmethod
    def validate_pagination(response, page_size):
        assert len(response.json()) <= page_size, f"Expected at most {page_size} items, but got {len(response.json())}"

    @staticmethod
    def validate_sorting(response, key, order='asc'):
        items = response.json()
        sorted_items = sorted(items, key=lambda x: x[key], reverse=(order == 'desc'))
        assert items == sorted_items, f"Expected items sorted by {key} in {order} order"

    @staticmethod
    def api_file_upload(url, file_path, headers=None):
        with open(file_path, 'rb') as file:
            files = {'file': file}
            response = requests.post(url, headers=headers, files=files)
        return response

    @staticmethod
    def validate_response_structure(response, structure):
        assert set(response.json().keys()) == set(structure), f"Expected structure {structure}, but got {response.json().keys()}"
