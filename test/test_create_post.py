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


def setup_module():
    global TOKEN

    TOKEN = Login().get_token()


@pytest.mark.acceptance_testing
@pytest.mark.smoke_testing
@pytest.mark.regression_testing
@allure.suite("negative_testing")
@allure.suite("regression_testing")
@allure.suite("smoke_testing")
def test_create_post():
    url = config('URL')
    crud_post = CrudPost(TOKEN)
    payload = load_json_expected_result("test/resources/resource_create_test/payload_create_post.json")
    response = crud_post.create_post(url, payload)

    assert_that(response.status_code).is_equal_to(http.HTTPStatus.CREATED)


@pytest.mark.acceptance_testing
@pytest.mark.regression_testing
@allure.suite("negative_testing")
@allure.suite("regression_testing")
def test_create_post_with_a_valid_id():
    url = config('URL')
    crud_post = CrudPost(TOKEN)
    payload = load_json_expected_result("test/resources/resource_create_test/payload_create_post_valid_id.json")
    response = crud_post.create_post(url, payload)
    response_text = json.loads(response.text)

    assert_that(response.status_code).is_equal_to(http.HTTPStatus.CREATED)
    assert_that(response_text['id']).is_instance_of(int)


@pytest.mark.acceptance_testing
@pytest.mark.regression_testing
@allure.suite("negative_testing")
@allure.suite("regression_testing")
def test_create_post_with_a_publish_status():
    url = config('URL')
    crud_post = CrudPost(TOKEN)
    payload = load_json_expected_result("test/resources/resource_create_test/payload_create_post_publish_status.json")
    response = crud_post.create_post(url, payload)
    response_text = json.loads(response.text)

    assert_that(response_text['status']).is_equal_to("publish")


@pytest.mark.negative_testing
@pytest.mark.regression_testing
@allure.suite("negative_testing")
@allure.suite("regression_testing")
def test_create_post_with_standard_format_by_default():

    url = config('URL')
    crud_post = CrudPost(TOKEN)
    payload = load_json_expected_result("test/resources/resource_create_test/payload_create_post_default_standard_format.json")
    response = crud_post.create_post(url, payload)
    response_text = json.loads(response.text)

    assert_that(response_text['format']).is_equal_to("standard")


@pytest.mark.negative_testing
@pytest.mark.regression_testing
@allure.suite("negative_testing")
@allure.suite("regression_testing")
def test_create_post_with_void_title():

    url = config('URL')
    payload = load_json_expected_result("test/resources/resource_create_test/payload_create_post_void_title.json")
    crud_post = CrudPost(TOKEN)
    response = crud_post.create_post(url, payload)
    response_text = json.loads(response.text)

    assert_that(response.status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)


@pytest.mark.negative_testing
@pytest.mark.regression_testing
@allure.suite("negative_testing")
@allure.suite("regression_testing")
def test_create_post_with_void_status():
    url = config('URL')
    payload = load_json_expected_result("test/resources/resource_create_test/payload_create_post_void_status.json")
    crud_post = CrudPost(TOKEN)
    response = crud_post.create_post(url, payload)
    response_text = json.loads(response.text)

    assert_that(response.status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
    assert_that(response_text['data']['details']['status']['code']).is_equal_to('rest_not_in_enum')
    assert_that(response_text['data']['details']['status']['data']).is_equal_to(None)


@pytest.mark.negative_testing
@pytest.mark.regression_testing
@allure.suite("negative_testing")
@allure.suite("regression_testing")
def test_create_post_with_invalid_author_id():

    url = config('URL')
    payload = load_json_expected_result("test/resources/resource_create_test/payload_create_post_invalid_author_id.json")
    crud_post = CrudPost(TOKEN)
    response = crud_post.create_post(url, payload)
    response_text = json.loads(response.text)

    assert_that(response.status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)


