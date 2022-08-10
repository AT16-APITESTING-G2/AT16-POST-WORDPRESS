#
# @test_retrieve_post.py Copyright (c) 2022 Jalasoft
# 2643 Av Melchor Perez de Olguin , Colquiri Sud, Cochabamba, Bolivia.
# add direccion de jala la paz>
# All rights reserved
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

import allure
import pytest
from http import HTTPStatus
from assertpy import assert_that
from model.crud_post import CrudPost
from decouple import config
import json
from model.login import Login
from utils.schema_validator import SchemaValidator

TOKEN = None


def load_json_expected_result(path):

    with open(path) as file_json:
        file_json_dict = json.load(file_json)
    return file_json_dict


@pytest.fixture(autouse=True)
@allure.title("Steps")
def setup_prerequisites():
    global TOKEN
    global ID_POST

    URL = config("URL")
    payload = load_json_expected_result("resources/resource_retrieve_test/payload_create_post.json")
    TOKEN = Login().get_token()
    crud_post = CrudPost(TOKEN)

    api_request_response = json.loads((crud_post.create_post(URL, payload)).response.text)
    ID_POST = api_request_response['id']
    allure.attach(str(ID_POST), 'ID post created:', allure.attachment_type.TEXT)
    allure.attach(str(TOKEN), 'Token', allure.attachment_type.TEXT)
    yield
    crud_post.delete_post(URL, ID_POST)
    allure.attach(str(ID_POST), 'ID post deleted:', allure.attachment_type.TEXT)


@allure.severity("critical")
@allure.suite("sanity_testing")
@allure.suite("acceptance_testing")
@allure.suite("regression_testing")
@allure.suite("smoke_testing")
@allure.epic("sanity_testing")
@allure.epic("acceptance_testing")
@allure.epic("regression_testing")
@allure.epic("smoke_testing")
@allure.link('https://apitestpost16.atlassian.net/browse/AP-31',
             name="https://apitestpost16.atlassian.net/browse/AP-31")
@allure.title("Retrieve a post")
@allure.step("Retrieve an existing Post")
@allure.description("Verify that the Post end point return an existing post")
def test_retrieve_an_existing_post():
    URL = config('URL')
    payload = {}
    crud_post = CrudPost(TOKEN)
    api = crud_post.retrieve_post(URL, ID_POST)
    headers = {
        "Url": str(api.request.url),
        "Method": str(api.request.method),
        "Authorization": str(api.request.headers['Authorization'])
    }
    allure.attach(json.dumps(headers, indent=4), 'Headers:', allure.attachment_type.JSON)
    allure.attach(json.dumps(payload, indent=4), 'Payload:', allure.attachment_type.JSON)
    response_text = json.loads(api.response.text)
    allure.attach(json.dumps(response_text, indent=4), 'JSON Response', allure.attachment_type.JSON)
    assert_that(api.response.status_code).is_equal_to(HTTPStatus.OK)
    allure.attach(str(api.response.status_code), 'Status code return', allure.attachment_type.TEXT)
    assert_that(response_text).contains('id')
    assert_that(response_text['id']).is_instance_of(int)
    assert_that(response_text['id']).is_equal_to(ID_POST)
    allure.attach(str(response_text['id']), 'Post id:', allure.attachment_type.TEXT)


@allure.severity("critical")
@allure.suite("security_testing")
@allure.suite("sanity_testing")
@allure.suite("regression_testing")
@allure.epic("security_testing")
@allure.epic("sanity_testing")
@allure.epic("regression_testing")
@allure.epic("negative_testing")
@allure.link('https://apitestpost16.atlassian.net/browse/AP-28',
             name="https://apitestpost16.atlassian.net/browse/AP-28")
@allure.title("Retrieve a post with a bad token")
@allure.step("Retrieve a post with a bad token")
@allure.description("Verify that when it sends a bad token, the 401 status is returned")
def test_retrieve_a_post_with_a_bad_token():
    URL = config('URL')
    TOKEN = "Bearer abc12345"
    crud_post = CrudPost(TOKEN)
    payload = {}
    api = crud_post.retrieve_post(URL, ID_POST)
    headers = {
        "Url": str(api.request.url),
        "Method": str(api.request.method),
        "Authorization": str(api.request.headers['Authorization'])
    }
    allure.attach(json.dumps(headers, indent=4), 'Headers:', allure.attachment_type.JSON)
    allure.attach(json.dumps(payload, indent=4), 'Payload:', allure.attachment_type.JSON)
    response_text = json.loads(api.response.text)
    allure.attach(json.dumps(response_text, indent=4), 'JSON Response', allure.attachment_type.JSON)
    assert_that(api.response.status_code).is_equal_to(HTTPStatus.UNAUTHORIZED)
    assert_that(response_text).contains('code')
    assert_that(response_text['code']).is_equal_to('401')
    allure.attach(str(api.response.status_code), 'Status code return', allure.attachment_type.TEXT)


@allure.severity("critical")
@allure.suite("sanity_testing")
@allure.suite("regression_testing")
@allure.epic("sanity_testing")
@allure.epic("regression_testing")
@allure.epic("negative_testing")
@allure.link('https://apitestpost16.atlassian.net/browse/AP-29',
             name="https://apitestpost16.atlassian.net/browse/AP-29")
@allure.title("Retrieve a post with a bad Id")
@allure.step("Retrieve a post with a bad Id")
@allure.description("Verify that the Post end point return the 404 status code with a bad id")
def test_retrieve_a_post_with_a_bad_id():
    URL = config('URL')
    ID_POST = -1
    payload = {}
    crud_post = CrudPost(TOKEN)

    api = crud_post.retrieve_post(URL, ID_POST)
    headers = {
        "Url": str(api.request.url),
        "Method": str(api.request.method),
        "Authorization": str(api.request.headers['Authorization'])
    }
    allure.attach(json.dumps(headers, indent=4), 'Headers:', allure.attachment_type.JSON)
    allure.attach(json.dumps(payload, indent=4), 'Payload:', allure.attachment_type.JSON)
    response_text = json.loads(api.response.text)
    allure.attach(json.dumps(response_text, indent=4), 'JSON Response', allure.attachment_type.JSON)

    assert_that(api.response.status_code).is_equal_to(HTTPStatus.NOT_FOUND)
    allure.attach(str(api.response.status_code), 'Status code return', allure.attachment_type.TEXT)

    assert_that(response_text).contains('code')
    assert_that(response_text).contains('message')


@allure.severity("critical")
@allure.suite("sanity_testing")
@allure.suite("regression_testing")
@allure.epic("sanity_testing")
@allure.epic("regression_testing")
@allure.epic("negative_testing")
@allure.link('https://apitestpost16.atlassian.net/browse/AP-30',
             name="https://apitestpost16.atlassian.net/browse/AP-30")
@allure.title("Retrieve a post with a bad route")
@allure.step("Retrieve a post with a bad route")
@allure.description("Verify that the Post end point return the 404 status when it send a bad route")
def test_retrieve_a_post_with_a_bad_route():
    URL = '{}/bad_route'.format(config('URL'))
    payload = {}
    crud_post = CrudPost(TOKEN)

    api = crud_post.retrieve_post(URL, ID_POST)
    headers = {
        "Url": str(api.request.url),
        "Method": str(api.request.method),
        "Authorization": str(api.request.headers['Authorization'])
    }
    allure.attach(json.dumps(headers, indent=4), 'Headers:', allure.attachment_type.JSON)
    allure.attach(json.dumps(payload, indent=4), 'Payload:', allure.attachment_type.JSON)
    response_text = json.loads(api.response.text)
    allure.attach(json.dumps(response_text, indent=4), 'JSON Response', allure.attachment_type.JSON)
    assert_that(api.response.status_code).is_equal_to(HTTPStatus.NOT_FOUND)
    allure.attach(str(api.response.status_code), 'Status code return', allure.attachment_type.TEXT)
    assert_that(response_text).contains('code')
    assert_that(response_text['code']).is_equal_to('rest_no_route')
    assert_that(response_text).contains('message')
    assert_that(response_text['message']).is_equal_to('No route was found matching the URL and request method.')


@allure.severity("normal")
@allure.suite("sanity_testing")
@allure.suite("regression_testing")
@allure.epic("sanity_testing")
@allure.epic("regression_testing")
@allure.link('https://apitestpost16.atlassian.net/browse/AP-27',
             name="https://apitestpost16.atlassian.net/browse/AP-27")
@allure.title("Validate the schema of Retrieve Post")
@allure.step("Validate the schema of Retrieve Post")
@allure.description("Verify that the response schema is valid")
def test_retrieve_schema_validator():
    URL = config('URL')
    payload = {}
    crud_post = CrudPost(TOKEN)
    api = crud_post.retrieve_post(URL, ID_POST)
    headers = {
        "Url": str(api.request.url),
        "Method": str(api.request.method),
        "Authorization": str(api.request.headers['Authorization'])
    }
    allure.attach(json.dumps(headers, indent=4), 'Headers:', allure.attachment_type.JSON)
    allure.attach(json.dumps(payload, indent=4), 'Payload:', allure.attachment_type.JSON)
    response_text = json.loads(api.response.text)
    allure.attach(json.dumps(response_text, indent=4), 'JSON Response', allure.attachment_type.JSON)

    expected_schema = load_json_expected_result("resources/resource_retrieve_test/schema_retrieve_post.json")

    validator = SchemaValidator(expected_schema, True)

    is_validate = validator.validate(response_text)
    assert_that(api.response.status_code).is_equal_to(HTTPStatus.OK)
    allure.attach(str(api.response.status_code), 'Status code return', allure.attachment_type.TEXT)
    assert_that(is_validate).is_true()
    allure.attach(json.dumps(expected_schema, indent=4), 'Valid Schema to match', allure.attachment_type.JSON)

