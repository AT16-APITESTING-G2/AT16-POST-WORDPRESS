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


def setup_module():
    global TOKEN

    TOKEN = Login().get_token()


def load_json_expected_result(path):

    with open(path) as file_json:
        file_json_dict = json.load(file_json)
    return file_json_dict


@pytest.mark.aceptance_testing
def test_delete_post():
    url = config('URL')
    id_post = config('ID_POST')
    crud_post = CrudPost(TOKEN)
    response = crud_post.delete_post(url, id_post)
    assert_that(response.status_code).is_equal_to(http.HTTPStatus.OK)


@pytest.mark.negative_testing
def test_delete_post_status_unauthorized():
    url = config('URL')
    id_post = config('ID_POST_404')
    crud_post = CrudPost("")

    response_str_void = crud_post.delete_post(url, id_post)
    assert_that(response_str_void.status_code).is_equal_to(http.HTTPStatus.UNAUTHORIZED)


@pytest.mark.aceptance_testing
def test_delete_post_status_void_id():
    url = config('URL')
    id_post = ''
    crud_post = CrudPost(TOKEN)

    response_str_void = crud_post.delete_post(url, id_post)
    assert_that(response_str_void.status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)


@pytest.mark.aceptance_testing
def test_delete_post_bad_url():
    url = 'http://localhost/wordpress/wp-json/wp/v2/posts/36'
    id_post = config('ID_POST_405')
    crud_post = CrudPost(TOKEN)
    response = crud_post.delete_post(url, id_post)

    assert_that(response.status_code).is_equal_to(http.HTTPStatus.METHOD_NOT_ALLOWED)


@pytest.mark.aceptance_testing
def test_delete_post_bad_id():
    url = config('URL')
    id_post = config('ID_POST_BAD_ID')
    crud_post = CrudPost(TOKEN)

    response = crud_post.delete_post(url, id_post)
    assert_that(response.status_code).is_equal_to(http.HTTPStatus.GONE)


@pytest.mark.aceptance_testing
@pytest.mark.endtoend_testing
def test_create_and_delete_post():
    url_created = config('URL_CREATED')
    crud_post = CrudPost(TOKEN)
    payload = load_json_expected_result("resources/resource_delete_test/payload_delete_post.json")
    response = crud_post.create_post(url_created, payload)
    assert_that(response.status_code).is_equal_to(http.HTTPStatus.CREATED)
    url = config('URL')
    id_response = json.loads(response.text)['id']
    id_post = f"/{id_response}"
    response_deleted = crud_post.delete_post(url, id_post)
    assert_that(response_deleted.status_code).is_equal_to(http.HTTPStatus.OK)
