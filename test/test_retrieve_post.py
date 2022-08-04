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

import pytest
import allure
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


def setup_module():

    global TOKEN

    TOKEN = Login().get_token()


@pytest.mark.sanity_testing
@pytest.mark.acceptance_testing
@pytest.mark.regression_testing
@pytest.mark.smoke_testing
@allure.suite("sanity_testing")
@allure.suite("acceptance_testing")
@allure.suite("smoke_testing")
@allure.suite("regression_testing")
def test_retrieve_an_existing_post():

    URL = config('URL')
    ID_POST = config('ID_POST')

    crud_post = CrudPost(TOKEN)
    api_request_response = crud_post.retrieve_post(URL, ID_POST)

    response_text = json.loads(api_request_response.text)

    assert_that(api_request_response.status_code).is_equal_to(HTTPStatus.OK)
    assert_that(response_text).contains('id')
    assert_that(response_text['id']).is_instance_of(int)
    # assert_that(response_text['id']).is_equal_to(108)


@pytest.mark.security_testing
@pytest.mark.sanity_testing
@pytest.mark.regression_testing
@allure.suite("security_testing")
@allure.suite("sanity_testing")
@allure.suite("regression_testing")
def test_retrieve_a_post_with_a_bad_token():

    URL = config('URL')
    ID_POST = config('ID_POST')
    TOKEN = "Bearer abc12345"
    crud_post = CrudPost(TOKEN)

    api_request_response = crud_post.retrieve_post(URL, ID_POST)
    print(api_request_response)
    response_text = json.loads(api_request_response.text)

    assert_that(api_request_response.status_code).is_equal_to(HTTPStatus.UNAUTHORIZED)
    assert_that(response_text).contains('code')
    assert_that(response_text['code']).is_equal_to('401')


@pytest.mark.sanity_testing
@pytest.mark.blackbox_testing
@pytest.mark.regression_testing
@allure.suite("sanity_testing")
@allure.suite("blackbox_testing")
@allure.suite("regression_testing")
def test_retrieve_a_post_with_a_bad_id():

    URL = config('URL')
    ID_POST = '/900'

    crud_post = CrudPost(TOKEN)

    api_request_response = crud_post.retrieve_post(URL, ID_POST)

    response_text = json.loads(api_request_response.text)

    assert_that(api_request_response.status_code).is_equal_to(HTTPStatus.NOT_FOUND)
    assert_that(response_text).contains('code')
    assert_that(response_text['code']).is_equal_to('rest_post_invalid_id')
    assert_that(response_text).contains('message')
    assert_that(response_text['message']).is_equal_to('Invalid post ID.')


@pytest.mark.sanity_testing
@pytest.mark.blackbox_testing
@pytest.mark.regression_testing
@allure.suite("sanity_testing")
@allure.suite("blackbox_testing")
@allure.suite("regression_testing")
def test_retrieve_a_post_with_a_bad_route():

    URL = '{}/bad_route'.format(config('URL'))
    ID_POST = config('ID_POST')

    crud_post = CrudPost(TOKEN)

    api_request_response = crud_post.retrieve_post(URL, ID_POST)

    response_text = json.loads(api_request_response.text)

    assert_that(api_request_response.status_code).is_equal_to(HTTPStatus.NOT_FOUND)
    assert_that(response_text).contains('code')
    assert_that(response_text['code']).is_equal_to('rest_no_route')
    assert_that(response_text).contains('message')
    assert_that(response_text['message']).is_equal_to('No route was found matching the URL and request method.')


@pytest.mark.sanity_testing
@pytest.mark.blackbox_testing
@pytest.mark.regression_testing
@allure.suite("sanity_testing")
@allure.suite("blackbox_testing")
@allure.suite("regression_testing")
def test_retrieve_schema_validator():
    URL = config('URL')
    ID_POST = config('ID_POST')

    crud_post = CrudPost(TOKEN)
    api_request_response = crud_post.retrieve_post(URL, ID_POST)

    response_text = json.loads(api_request_response.text)

    expected_schema = load_json_expected_result("test/resources/resource_retrieve_test/schema_retrieve_post.json")

    validator = SchemaValidator(expected_schema, False)

    is_validate = validator.validate(response_text)
    assert_that(api_request_response.status_code).is_equal_to(HTTPStatus.OK)
    assert_that(is_validate).is_true()
