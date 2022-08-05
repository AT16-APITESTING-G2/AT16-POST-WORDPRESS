#
# @test_update_post.py Copyright (c) 2022 Jalasoft
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

import json
import allure
import pytest
from http import HTTPStatus
from assertpy.assertpy import assert_that
from model.crud_post import CrudPost
from decouple import config
from model.login import Login
from test.test_create_post import load_json_expected_result


@pytest.fixture(autouse=True)
def setup_prerequisites():
    global TOKEN
    global ID_POST

    URL = config("URL")
    payload = load_json_expected_result("resources/resource_retrieve_test/payload_create_post.json")
    TOKEN = Login().get_token()
    crud_post = CrudPost(TOKEN)

    api_request_response = json.loads((crud_post.create_post(URL, payload)).text)
    ID_POST = api_request_response['id']
    yield
    crud_post.delete_post(URL, ID_POST)


@pytest.mark.acceptance_testing
@pytest.mark.smoke_testing
@pytest.mark.regression_testing
@allure.severity("critical")
@allure.suite("smoke_testing")
@allure.suite("regression_testing")
@allure.suite("acceptance_testing")
@allure.epic("smoke_testing")
@allure.epic("regression_testing")
@allure.epic("acceptance_testing")
def test_update_post():
    url = config('URL')

    crud_post = CrudPost(TOKEN)
    payload = load_json_expected_result("resources/resource_update_test/payload_update_post.json")
    response = crud_post.update_post(url, ID_POST, payload)
    response_text = json.loads(response.text)

    assert_that(response.status_code).is_equal_to(HTTPStatus.OK)
    assert_that(response_text).contains('id')
    assert_that(response_text['id']).is_instance_of(int)


@pytest.mark.functional_testing
@pytest.mark.regression_testing
@allure.severity("minor")
@allure.suite("functional_testing")
@allure.suite("regression_testing")
@allure.epic("functional_testing")
@allure.epic("regression_testing")
def test_update_author_post_field():
    url = config('URL')

    crud_post = CrudPost(TOKEN)
    payload = load_json_expected_result("resources/resource_update_test/payload_update_author_post.json")
    response = crud_post.update_post(url, ID_POST, payload)
    response_text = json.loads(response.text)

    assert_that(response.status_code).is_equal_to(HTTPStatus.OK)
    assert_that(response_text).contains('author')
    assert_that(response_text['author']).is_instance_of(int)


@pytest.mark.functional_testing
@pytest.mark.regression_testing
@allure.severity("minor")
@allure.suite("functional_testing")
@allure.suite("regression_testing")
@allure.epic("functional_testing")
@allure.epic("regression_testing")
def test_update_status_post_field():
    url = config('URL')

    crud_post = CrudPost(TOKEN)
    payload = load_json_expected_result("resources/resource_update_test/payload_update_status_post.json")
    response = crud_post.update_post(url, ID_POST, payload)
    response_text = json.loads(response.text)

    assert_that(response.status_code).is_equal_to(HTTPStatus.OK)
    assert_that(response_text).contains('status')
    assert_that(response_text['status']).is_not_empty()


@pytest.mark.functional_testing
@pytest.mark.regression_testing
@allure.severity("normal")
@allure.suite("functional_testing")
@allure.suite("regression_testing")
@allure.epic("functional_testing")
@allure.epic("regression_testing")
def test_update_comment_status_post():
    url = config('URL')

    crud_post = CrudPost(TOKEN)
    payload = load_json_expected_result("resources/resource_update_test/payload_update_comment_status_post.json")
    response = crud_post.update_post(url, ID_POST, payload)
    response_text = json.loads(response.text)

    assert_that(response.status_code).is_equal_to(HTTPStatus.OK)
    assert_that(response_text).contains('comment_status')
    assert_that(response_text['comment_status']).is_not_empty()


@pytest.mark.negative_testing
@pytest.mark.regression_testing
@allure.severity("critical")
@allure.suite("negative_testing")
@allure.suite("regression_testing")
@allure.epic("negative_testing")
@allure.epic("regression_testing")
def test_update_post_with_invalid_id():
    url = config('URL')
    id = 9999999

    crud_post = CrudPost(TOKEN)
    payload = load_json_expected_result("resources/resource_update_test/payload_update_invalid_id.json")
    response = crud_post.update_post(url, id, payload)
    response_text = json.loads(response.text)

    assert_that(response.status_code).is_equal_to(HTTPStatus.NOT_FOUND)
    assert_that(response_text).contains('code')
    assert_that(response_text['code']).is_equal_to("rest_post_invalid_id")


@pytest.mark.negative_testing
@pytest.mark.regression_testing
@allure.severity("minor")
@allure.suite("negative_testing")
@allure.suite("regression_testing")
@allure.epic("negative_testing")
@allure.epic("regression_testing")
def test_update_status_field_with_invalid_value():
    url = config('URL')

    crud_post = CrudPost(TOKEN)
    payload = load_json_expected_result("resources/resource_update_test/payload_update_invalid_status_field.json")
    response = crud_post.update_post(url, ID_POST, payload)
    response_text = json.loads(response.text)

    assert_that(response.status_code).is_equal_to(HTTPStatus.BAD_REQUEST)
    assert_that(response_text).contains('code')
    assert_that(response_text['code']).is_equal_to("rest_invalid_param")


@pytest.mark.negative_testing
@pytest.mark.regression_testing
@allure.severity("minor")
@allure.suite("negative_testing")
@allure.suite("regression_testing")
@allure.epic("negative_testing")
@allure.epic("regression_testing")
def test_update_comment_status_field_with_invalid_value():
    url = config('URL')

    crud_post = CrudPost(TOKEN)
    payload = load_json_expected_result("resources/resource_update_test/payload_update_invalid_status_field.json")
    response = crud_post.update_post(url, ID_POST, payload)
    response_text = json.loads(response.text)

    assert_that(response.status_code).is_equal_to(HTTPStatus.BAD_REQUEST)
    assert_that(response_text).contains('code')
    assert_that(response_text['code']).is_equal_to("rest_invalid_param")


@pytest.mark.negative_testing
@pytest.mark.regression_testing
@allure.severity("minor")
@allure.suite("negative_testing")
@allure.suite("regression_testing")
@allure.epic("negative_testing")
@allure.epic("regression_testing")
def test_update_invalid_ping_status_field():
    url = config('URL')

    crud_post = CrudPost(TOKEN)
    payload = load_json_expected_result("resources/resource_update_test/payload_update_invalid_ping_status_field.json")
    response = crud_post.update_post(url, ID_POST, payload)
    response_text = json.loads(response.text)

    assert_that(response.status_code).is_equal_to(HTTPStatus.BAD_REQUEST)
    assert_that(response_text).contains('code')
    assert_that(response_text['code']).is_equal_to("rest_invalid_param")
