#
# @test_create_post.py Copyright (c) 2022 Jalasoft
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

import http
import json
import allure
import pytest
from assertpy import assert_that
from model.crud_post import CrudPost
from decouple import config
from model.login import Login


def load_json_expected_result(path):

    with open(path) as file_json:
        file_json_dict = json.load(file_json)
    return file_json_dict


@pytest.fixture(autouse=True)
def setup_prerequisites():
    global TOKEN
    TOKEN = Login().get_token()


@pytest.fixture
def teardown_delete_test():
    global ID_POST
    pass
    yield
    URL = config("URL")
    crud_post = CrudPost(TOKEN)
    crud_post.delete_post(URL, ID_POST)


@allure.severity("critical")
@allure.suite("acceptance_testing")
@allure.suite("regression_testing")
@allure.suite("smoke_testing")
@allure.epic("acceptance_testing")
@allure.epic("regression_testing")
@allure.epic("smoke_testing")
@allure.link('https://apitestpost16.atlassian.net/browse/AP-39', name="Verify the response is 200 when a post is "
                                                                      "update successfully")
@allure.title("Verify that http status code is 201(CREATED).")
@allure.step("Create a new post in a wordpress project")
@allure.description("This test case is used to create a new wordpress post")
def test_create_post():

    url = config('URL')
    crud_post = CrudPost(TOKEN)
    payload = load_json_expected_result("resources/resource_create_test/payload_create_post.json")
    api = crud_post.create_post(url, payload)
    headers = {
        "Url": str(api.request.url),
        "Method": str(api.request.method),
        "Authorization": str(api.request.headers['Authorization'])
    }
    allure.attach(json.dumps(headers, indent=4), 'Headers:', allure.attachment_type.JSON)
    allure.attach(json.dumps(payload, indent=4), 'Payload:', allure.attachment_type.JSON)
    response_dict = json.loads(api.response.text)
    allure.attach(json.dumps(response_dict, indent=4), 'JSON Response', allure.attachment_type.JSON)
    assert_that(api.response.status_code).is_equal_to(http.HTTPStatus.CREATED)
    allure.attach(str(api.response.status_code), 'Status code return', allure.attachment_type.TEXT)
    id_post = response_dict['id']
    crud_post.delete_post(url, id_post)



@allure.severity("critical")
@allure.suite("acceptance_testing")
@allure.suite("regression_testing")
@allure.suite("sanity_testing")
@allure.epic("acceptance_testing")
@allure.epic("regression_testing")
@allure.epic("sanity_testing")
@allure.link('https://apitestpost16.atlassian.net/browse/AP-40', name="Verify that “id“ of the request "
                                                                      "is “int” type. ")
@allure.title("Verify that “id“ of the request is “int” type.")
@allure.step("Create a new post with a id of int type")
@allure.description("verify that that a new post response have a valid type id")
def test_create_post_with_a_valid_id():
    url = config('URL')
    crud_post = CrudPost(TOKEN)
    payload = load_json_expected_result("resources/resource_create_test/payload_create_post_valid_id.json")
    api = crud_post.create_post(url, payload)
    headers = {
        "Url": str(api.request.url),
        "Method": str(api.request.method),
        "Authorization": str(api.request.headers['Authorization'])
    }
    allure.attach(json.dumps(headers, indent=4), 'Headers:', allure.attachment_type.JSON)
    allure.attach(json.dumps(payload, indent=4), 'Payload:', allure.attachment_type.JSON)
    response_text = json.loads(api.response.text)
    allure.attach(json.dumps(response_text, indent=4), 'JSON Response', allure.attachment_type.JSON)
    assert_that(api.response.status_code).is_equal_to(http.HTTPStatus.CREATED)
    allure.attach(str(api.response.status_code), 'Status code return', allure.attachment_type.TEXT)
    assert_that(response_text['id']).is_instance_of(int)
    allure.attach(str(response_text['id']), 'Post id:', allure.attachment_type.TEXT)
    id_post = response_text['id']
    crud_post.delete_post(url, id_post)


@allure.severity("trivial")
@allure.suite("acceptance_testing")
@allure.suite("regression_testing")
@allure.epic("acceptance_testing")
@allure.epic("regression_testing")
@allure.link('https://apitestpost16.atlassian.net/browse/AP-41', name="Verify that the post response have "                                                                  "a status publish.")
@allure.title("Verify that the post response have a status publish.")
@allure.step("Create a new post with a status publish")
@allure.description("This is a test case to verify that a new post created have a status publish")
def test_create_post_with_a_publish_status():
    url = config('URL')
    crud_post = CrudPost(TOKEN)
    payload = load_json_expected_result("resources/resource_create_test/payload_create_post_publish_status.json")
    api = crud_post.create_post(url, payload)
    headers = {
        "Url": str(api.request.url),
        "Method": str(api.request.method),
        "Authorization": str(api.request.headers['Authorization'])
    }
    allure.attach(json.dumps(headers, indent=4), 'Headers:', allure.attachment_type.JSON)
    allure.attach(json.dumps(payload, indent=4), 'Payload:', allure.attachment_type.JSON)
    response_text = json.loads(api.response.text)
    allure.attach(json.dumps(response_text, indent=4), 'JSON Response', allure.attachment_type.JSON)
    assert_that(response_text['status']).is_equal_to("publish")
    allure.attach(str(response_text['status']), 'Status post by default', allure.attachment_type.TEXT)
    id_post = response_text['id']
    crud_post.delete_post(url, id_post)


@allure.severity("minor")
@allure.suite("acceptance_testing")
@allure.suite("regression_testing")
@allure.epic("regression_testing")
@allure.epic("acceptance_testing")
@allure.link('https://apitestpost16.atlassian.net/browse/AP-14', name="Verify the response have a standard"
                                                                      "format by default")
@allure.title("Verify the response have a standard format by default")
@allure.step("Create a new post with a forma by default")
@allure.description("This a test case to verify that a any new post is created with a stanadard format by default")
def test_create_post_with_standard_format_by_default():

    url = config('URL')
    crud_post = CrudPost(TOKEN)
    payload = load_json_expected_result("resources/resource_create_test/payload_create_post_default_standard_format.json")
    api = crud_post.create_post(url, payload)
    headers = {
        "Url": str(api.request.url),
        "Method": str(api.request.method),
        "Authorization": str(api.request.headers['Authorization'])
    }
    allure.attach(json.dumps(headers, indent=4), 'Headers:', allure.attachment_type.JSON)
    allure.attach(json.dumps(payload, indent=4), 'Payload:', allure.attachment_type.JSON)
    response_text = json.loads(api.response.text)
    allure.attach(json.dumps(response_text, indent=4), 'JSON Response', allure.attachment_type.JSON)
    assert_that(response_text['format']).is_equal_to("standard")
    allure.attach(str(response_text['format']), 'format post by default', allure.attachment_type.TEXT)
    id_post = response_text['id']
    crud_post.delete_post(url, id_post)


@allure.severity("minor")
@allure.suite("negative_testing")
@allure.suite("regression_testing")
@allure.epic("negative_testing")
@allure.epic("regression_testing")
@allure.link('https://apitestpost16.atlassian.net/browse/AP-14', name="Verify the response is 400 when the post "
                                                                      "is created with a void title")
@allure.title("Verify the response is 401 when the post is created with a void title")
@allure.step("Create a new post wit a void title")
@allure.description("This is a negative test case that is used to verify that response is 401(Bad Request) when the title is void")
def test_create_post_with_void_title():

    url = config('URL')
    payload = load_json_expected_result("resources/resource_create_test/payload_create_post_void_title.json")
    crud_post = CrudPost(TOKEN)
    api = crud_post.create_post(url, payload)
    headers = {
        "Url": str(api.request.url),
        "Method": str(api.request.method),
        "Authorization": str(api.request.headers['Authorization'])
    }
    allure.attach(json.dumps(headers, indent=4), 'Headers:', allure.attachment_type.JSON)
    allure.attach(json.dumps(payload, indent=4), 'Payload:', allure.attachment_type.JSON)
    assert_that(api.response.status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
    allure.attach(str(api.response.status_code), 'Status code return', allure.attachment_type.TEXT)

@allure.severity("critical")
@allure.suite("negative_testing")
@allure.suite("regression_testing")
@allure.suite("sanity_testing")
@allure.epic("negative_testing")
@allure.epic("regression_testing")
@allure.epic("sanity_testing")
@allure.link('https://apitestpost16.atlassian.net/browse/AP-14', name="Verify the response is 400 and when the post "
                                                                      "is created with a void status")
@allure.title("Verify the response is 400 and when the post is created with a void status")
@allure.step("Create a new post with a void status")
@allure.description("This is a negative test case to verify that the create post response with a void returns a status code 400.")
def test_create_post_with_void_status():
    url = config('URL')
    payload = load_json_expected_result("resources/resource_create_test/payload_create_post_void_status.json")
    crud_post = CrudPost(TOKEN)
    api = crud_post.create_post(url, payload)
    headers = {
        "Url": str(api.request.url),
        "Method": str(api.request.method),
        "Authorization": str(api.request.headers['Authorization'])
    }

    allure.attach(json.dumps(headers, indent=4), 'Headers:', allure.attachment_type.JSON)
    allure.attach(json.dumps(payload, indent=4), 'Payload:', allure.attachment_type.JSON)
    response_text = json.loads(api.response.text)
    allure.attach(json.dumps(response_text, indent=4), 'JSON Response', allure.attachment_type.JSON)
    assert_that(api.response.status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
    assert_that(response_text['data']['details']['status']['code']).is_equal_to('rest_not_in_enum')
    allure.attach(str(response_text['data']['details']['status']['code']), 'Code to void status', allure.attachment_type.TEXT)
    assert_that(response_text['data']['details']['status']['data']).is_equal_to(None)
    allure.attach(str(response_text['data']['details']['status']['data']), 'Null status', allure.attachment_type.TEXT)

@allure.severity("critical")
@allure.suite("negative_testing")
@allure.suite("regression_testing")
@allure.suite("sanity_testing")
@allure.suite("negative_testing")
@allure.suite("regression_testing")
@allure.epic("sanity_testing")
@allure.epic("negative_testing")
@allure.epic("regression_testing")
@allure.link('https://apitestpost16.atlassian.net/browse/AP-14', name="Verify the response is 400 and when the post "
                                                                      "is created with an invalid author id")
@allure.title("Verify the response is 400 and when the post is created with an invalid author id")
@allure.step("Create a new post with a invalid author id")
@allure.description("This is a negative test case to verify that the create post response with a invalid author id returns a status code 400.")
def test_create_post_with_invalid_author_id():

    url = config('URL')
    payload = load_json_expected_result("resources/resource_create_test/payload_create_post_invalid_author_id.json")
    crud_post = CrudPost(TOKEN)
    api = crud_post.create_post(url, payload)
    headers = {
        "Url": str(api.request.url),
        "Method": str(api.request.method),
        "Authorization": str(api.request.headers['Authorization'])
    }
    allure.attach(json.dumps(headers, indent=4), 'Headers:', allure.attachment_type.JSON)
    allure.attach(json.dumps(payload, indent=4), 'Payload:', allure.attachment_type.JSON)
    response_text = json.loads(api.response.text)
    allure.attach(json.dumps(response_text, indent=4), 'JSON Response', allure.attachment_type.JSON)
    assert_that(api.response.status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
    assert_that(response_text['code']).is_equal_to('rest_invalid_author')
    allure.attach(str(response_text['code']), 'Code to invalid author', allure.attachment_type.TEXT)
    assert_that(response_text['message']).is_equal_to('Invalid author ID.')
    allure.attach(str(response_text['message']), 'Message to invalid author', allure.attachment_type.TEXT)


@allure.severity("critical")
@allure.suite("security_testing")
@allure.suite("sanity_testing")
@allure.suite("regression_testing")
@allure.suite("negative_testing")
@allure.epic("security_testing")
@allure.epic("sanity_testing")
@allure.epic("regression_testing")
@allure.epic("negative_testing")
@allure.link('https://apitestpost16.atlassian.net/browse/AP-14', name="Verify the response is 401 and when the post "
                                                                      "is created with an invalid token")
@allure.title("Create ping status field post with an invalid value")
@allure.step("Steps create ping status field post with an invalid value")
@allure.description("This is a negative test case that is used to create a post with an invalid token.")
def test_create_post_with_a_bad_token():
    url = config('URL')
    token = "Bearer 2346jjj"
    crud_post = CrudPost(token)

    payload = load_json_expected_result("resources/resource_update_test/payload_update_post.json")
    api = crud_post.create_post(url, payload)
    headers = {
        "Url": str(api.request.url),
        "Method": str(api.request.method),
        "Authorization": str(api.request.headers['Authorization'])
    }
    allure.attach(json.dumps(headers, indent=4), 'Headers:', allure.attachment_type.JSON)
    allure.attach(json.dumps(payload, indent=4), 'Payload:', allure.attachment_type.JSON)
    response_text = json.loads(api.response.text)
    allure.attach(json.dumps(response_text, indent=4), 'JSON Response', allure.attachment_type.JSON)
    assert_that(api.response.status_code).is_equal_to(http.HTTPStatus.UNAUTHORIZED)
    allure.attach(str(api.response.status_code), 'Status code return', allure.attachment_type.TEXT)
    assert_that(response_text).contains('code')
    allure.attach(str(response_text['code']), 'Code assert', allure.attachment_type.TEXT)
    assert_that(response_text['code']).is_equal_to('401')
