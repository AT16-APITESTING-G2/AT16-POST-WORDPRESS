#
# @test_delete_post.py Copyright (c) 2022 Jalasoft
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
from decouple import config
from assertpy import assert_that
from model.crud_post import CrudPost
from model.login import Login


@pytest.fixture(autouse=True)
@allure.title("Steps")
def setup_prerequisites():
    global TOKEN
    global ID_POST

    URL = config("URL")
    payload = load_json_expected_result("resources/resource_delete_test/payload_delete_post.json")
    TOKEN = Login().get_token()
    crud_post = CrudPost(TOKEN)

    api_request_response = json.loads((crud_post.create_post(URL, payload)).response.text)
    ID_POST = api_request_response['id']
    allure.attach(str(ID_POST), 'ID post created:', allure.attachment_type.TEXT)
    allure.attach(str(TOKEN), 'Token', allure.attachment_type.TEXT)

@pytest.fixture
def teardown_delete_test():
    pass
    yield
    URL = config("URL")
    crud_post = CrudPost(TOKEN)
    crud_post.delete_post(URL, ID_POST)
    allure.attach(str(ID_POST), 'ID post deleted:', allure.attachment_type.TEXT)

def load_json_expected_result(path):

    with open(path) as file_json:
        file_json_dict = json.load(file_json)
    return file_json_dict


@pytest.mark.acceptance_testing
@pytest.mark.smoke_testing
@pytest.mark.regression_testing
@pytest.mark.sanity_testing
@allure.severity("critical")
@allure.suite("acceptance_testing")
@allure.suite("smoke_testing")
@allure.suite("regression_testing")
@allure.suite("sanity_testing")
@allure.epic("acceptance_testing")
@allure.epic("smoke_testing")
@allure.epic("regression_testing")
@allure.epic("sanity_testing")
@allure.title("delete post test")
@allure.step("delete happy path")
@allure.description("test case about delete post with his happy path status ok")
def test_delete_post():
    url = config('URL')
    crud_post = CrudPost(TOKEN)
    response = crud_post.delete_post(url, ID_POST)
    assert_that(response.response.status_code).is_equal_to(http.HTTPStatus.OK)
    headers = {
        "Url": str(response.request.url),
        "Method": str(response.request.method),
        "Authorization": str(response.request.headers['Authorization'])
    }
    allure.attach(json.dumps(headers, indent=4), 'Headers:', allure.attachment_type.JSON)
    response_text = json.loads(response.response.text)
    allure.attach(json.dumps(response_text, indent=4), 'JSON Response', allure.attachment_type.JSON)
    allure.attach(str(response.response.status_code), 'Status code return', allure.attachment_type.TEXT)
    allure.attach(str(response_text['id']), 'Id deleted:', allure.attachment_type.TEXT)

@pytest.mark.negative_testing
@pytest.mark.regression_testing
@pytest.mark.security_testing
@allure.severity("critical")
@allure.suite("negative_testing")
@allure.suite("regression_testing")
@allure.suite("security_testing")
@allure.epic("negative_testing")
@allure.epic("regression_testing")
@allure.epic("security_testing")
@allure.title("delete post bad token test")
@allure.step("delete in verification token")
@allure.description("test case about delete post with status is UNAUTHORIZED")
def test_delete_post_with_bad_token(teardown_delete_test):
    url = config('URL')
    TOKEN = "Bearer abc12345"
    crud_post = CrudPost(TOKEN)

    response_bad_id = crud_post.delete_post(url, ID_POST)
    assert_that(response_bad_id.response.status_code).is_equal_to(http.HTTPStatus.UNAUTHORIZED)
    headers = {
        "Url": str(response_bad_id.request.url),
        "Method": str(response_bad_id.request.method),
        "Authorization": str(response_bad_id.request.headers['Authorization'])
    }
    allure.attach(json.dumps(headers, indent=4), 'Headers:', allure.attachment_type.JSON)
    response_text = json.loads(response_bad_id.response.text)
    allure.attach(json.dumps(response_text, indent=4), 'JSON Response', allure.attachment_type.JSON)
    allure.attach(str(response_bad_id.response.status_code), 'Status code return', allure.attachment_type.TEXT)


@pytest.mark.acceptance_testing
@pytest.mark.regression_testing
@allure.severity("critical")
@allure.suite("acceptance_testing")
@allure.suite("regression_testing")
@allure.epic("acceptance_testing")
@allure.epic("regression_testing")
@allure.title("delete post void id test")
@allure.step("delete post in verification id")
@allure.description("test case about delete post with void ID and received status NOT_FOUND")
def test_delete_post_with_void_id(teardown_delete_test):
    url = config('URL')
    id_post = -1
    crud_post = CrudPost(TOKEN)

    response_str_void = crud_post.delete_post(url, id_post)
    assert_that(response_str_void.response.status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)
    headers = {
        "Url": str(response_str_void.request.url),
        "Method": str(response_str_void.request.method),
        "Authorization": str(response_str_void.request.headers['Authorization'])
    }
    allure.attach(json.dumps(headers, indent=4), 'Headers:', allure.attachment_type.JSON)
    response_text = json.loads(response_str_void.response.text)
    allure.attach(json.dumps(response_text, indent=4), 'JSON Response', allure.attachment_type.JSON)
    allure.attach(str(response_str_void.response.status_code), 'Status code return', allure.attachment_type.TEXT)


@pytest.mark.acceptance_testing
@pytest.mark.regression_testing
@allure.severity("critical")
@allure.suite("acceptance_testing")
@allure.suite("regression_testing")
@allure.epic("acceptance_testing")
@allure.epic("regression_testing")
@allure.title("delete post bad url test")
@allure.step("delete post in verification url")
@allure.description("test case about delete post with bad url and received status NOT_FOUND")
def test_delete_post_with_bad_url(teardown_delete_test):
    url = "{}/{}".format(config("URL"), "bad")
    crud_post = CrudPost(TOKEN)
    response = crud_post.delete_post(url, ID_POST)

    assert_that(response.response.status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)
    headers = {
        "Url": str(response.request.url),
        "Method": str(response.request.method),
        "Authorization": str(response.request.headers['Authorization'])
    }
    allure.attach(json.dumps(headers, indent=4), 'Headers:', allure.attachment_type.JSON)
    response_text = json.loads(response.response.text)
    allure.attach(json.dumps(response_text, indent=4), 'JSON Response', allure.attachment_type.JSON)
    allure.attach(str(response.response.status_code), 'Status code return', allure.attachment_type.TEXT)


@pytest.mark.acceptance_testing
@pytest.mark.regression_testing
@allure.severity("normal")
@allure.suite("acceptance_testing")
@allure.suite("regression_testing")
@allure.epic("acceptance_testing")
@allure.epic("regression_testing")
@allure.title("delete post bad id test")
@allure.step("delete post in verification id")
@allure.description("test case about delete post with bad ID and received status GONE")
def test_delete_post_with_bad_id():
    url = config('URL')
    crud_post = CrudPost(TOKEN)

    crud_post.delete_post(url, ID_POST)
    second_response = crud_post.delete_post(url, ID_POST)
    assert_that(second_response.response.status_code).is_equal_to(http.HTTPStatus.GONE)
    headers = {
        "Url": str(second_response.request.url),
        "Method": str(second_response.request.method),
        "Authorization": str(second_response.request.headers['Authorization'])
    }
    allure.attach(json.dumps(headers, indent=4), 'Headers:', allure.attachment_type.JSON)
    response_text = json.loads(second_response.response.text)
    allure.attach(json.dumps(response_text, indent=4), 'JSON Response', allure.attachment_type.JSON)
    allure.attach(str(second_response.response.status_code), 'Status code return', allure.attachment_type.TEXT)


@pytest.mark.acceptance_testing
@pytest.mark.endtoend_testing
@pytest.mark.regression_testing
@pytest.mark.sanity_testing
@allure.severity("critical")
@allure.suite("acceptance_testing")
@allure.suite("endtoend_testing")
@allure.suite("regression_testing")
@allure.suite("sanity_testing")
@allure.epic("acceptance_testing")
@allure.epic("endtoend_testing")
@allure.epic("regression_testing")
@allure.epic("sanity_testing")
@allure.title("delete post create and delete test")
@allure.step("delete post in end to end test")
@allure.description("test case about delete post with new ID created and had status created and ok")
def test_create_and_delete_post(teardown_delete_test):
    url_created = config("URL")
    crud_post = CrudPost(TOKEN)
    payload = load_json_expected_result("resources/resource_delete_test/payload_delete_post.json")
    response = crud_post.create_post(url_created, payload)
    assert_that(response.response.status_code).is_equal_to(http.HTTPStatus.CREATED)

    url = config('URL')
    id_response = json.loads(response.response.text)['id']
    response_deleted = crud_post.delete_post(url, id_response)
    assert_that(response_deleted.response.status_code).is_equal_to(http.HTTPStatus.OK)
    headers_delete = {
        "Url": str(response_deleted.request.url),
        "Method": str(response_deleted.request.method),
        "Authorization": str(response_deleted.request.headers['Authorization'])
    }
    allure.attach(json.dumps(headers_delete, indent=4), 'Headers:', allure.attachment_type.JSON)
    response_text = json.loads(response_deleted.response.text)
    allure.attach(json.dumps(response_text, indent=4), 'JSON Response', allure.attachment_type.JSON)
    allure.attach(str(response.response.status_code), 'Status code return', allure.attachment_type.TEXT)
    allure.attach(str(response_text['id']), 'Id deleted:', allure.attachment_type.TEXT)
