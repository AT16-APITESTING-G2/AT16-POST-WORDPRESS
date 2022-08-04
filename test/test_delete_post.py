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
import pytest
from decouple import config
from assertpy import assert_that
from model.crud_post import CrudPost
from model.login import Login


@pytest.fixture(autouse=True)
def setup_prerequisites():
    global TOKEN
    global ID_POST

    URL = config("URL")
    payload = load_json_expected_result("resources/resource_delete_test/payload_delete_post.json")
    TOKEN = Login().get_token()
    crud_post = CrudPost(TOKEN)

    api_request_response = json.loads((crud_post.create_post(URL, payload)).text)
    ID_POST = api_request_response['id']


@pytest.fixture
def teardown_delete_test():
    pass
    yield
    URL = config("URL")
    crud_post = CrudPost(TOKEN)
    crud_post.delete_post(URL, ID_POST)

def load_json_expected_result(path):

    with open(path) as file_json:
        file_json_dict = json.load(file_json)
    return file_json_dict


@pytest.mark.aceptance_testing
def test_delete_post():
    url = config('URL')
    crud_post = CrudPost(TOKEN)
    response = crud_post.delete_post(url, ID_POST)
    assert_that(response.status_code).is_equal_to(http.HTTPStatus.OK)


@pytest.mark.negative_testing
def test_delete_post_status_unauthorized(teardown_delete_test):
    url = config('URL')
    TOKEN = "Bearer abc12345"
    crud_post = CrudPost(TOKEN)

    response_str_void = crud_post.delete_post(url, ID_POST)
    assert_that(response_str_void.status_code).is_equal_to(http.HTTPStatus.UNAUTHORIZED)


@pytest.mark.aceptance_testing
def test_delete_post_status_void_id(teardown_delete_test):
    url = config('URL')
    id_post = -1
    crud_post = CrudPost(TOKEN)

    response_str_void = crud_post.delete_post(url, id_post)
    assert_that(response_str_void.status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)


@pytest.mark.aceptance_testing
def test_delete_post_bad_url(teardown_delete_test):
    url = 'http://localhost/bad_database/wp-json/wp/v2/posts'
    crud_post = CrudPost(TOKEN)
    response = crud_post.delete_post(url, ID_POST)

    assert_that(response.status_code).is_equal_to(http.HTTPStatus.METHOD_NOT_ALLOWED)


@pytest.mark.aceptance_testing
def test_delete_post_bad_id():
    url = config('URL')
    crud_post = CrudPost(TOKEN)

    crud_post.delete_post(url, ID_POST)
    second_response = crud_post.delete_post(url, ID_POST)
    assert_that(second_response.status_code).is_equal_to(http.HTTPStatus.GONE)


@pytest.mark.aceptance_testing
@pytest.mark.endtoend_testing
def test_create_and_delete_post(teardown_delete_test):
    url_created = config("URL")
    crud_post = CrudPost(TOKEN)
    payload = load_json_expected_result("resources/resource_delete_test/payload_delete_post.json")
    response = crud_post.create_post(url_created, payload)
    assert_that(response.status_code).is_equal_to(http.HTTPStatus.CREATED)

    url = config('URL')
    id_response = json.loads(response.text)['id']
    response_deleted = crud_post.delete_post(url, id_response)
    assert_that(response_deleted.status_code).is_equal_to(http.HTTPStatus.OK)
