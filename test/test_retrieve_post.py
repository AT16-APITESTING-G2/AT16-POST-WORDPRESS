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

from http import HTTPStatus
from unittest import TestCase
from assertpy import assert_that
from crud_post import CrudPost
from decouple import config

from helpers.login import Login


class TestRetrievePost(TestCase):

    def test_retrieve_post(self):

        URL = config('URL')
        ID_POST = config('ID_POST')

        URI_TOKEN = config('URI_TOKEN')
        USER_NAME = config('USER_NAME')
        PASSWORD = config('PASSWORD')

        response_login = Login().login(URI_TOKEN, USER_NAME, PASSWORD).json()

        TOKEN = response_login['token_type'] + ' ' + response_login['jwt_token']

        crud_post = CrudPost()
        response_result = crud_post.retrieve_post(URL, TOKEN, ID_POST)

        assert_that(response_result.status_code).is_equal_to(HTTPStatus.OK)
        assert_that(response_result.json()).contains('id')
        assert_that(response_result.json()['id']).is_instance_of(int)
        assert_that(response_result.json()['id']).is_equal_to(54)

    def test_retrieve_post_with_bad_id(self):

        URL = config('URL')
        ID_POST = '/90'

        URI_TOKEN = config('URI_TOKEN')
        USER_NAME = config('USER_NAME')
        PASSWORD = config('PASSWORD')

        response_login = Login().login(URI_TOKEN, USER_NAME, PASSWORD).json()

        TOKEN = response_login['token_type'] + ' ' + response_login['jwt_token']

        crud_post = CrudPost()

        response_result = crud_post.retrieve_post(URL, TOKEN, ID_POST)
        assert_that(response_result.status_code).is_equal_to(HTTPStatus.NOT_FOUND)
        assert_that(response_result.json()).contains('code')
        assert_that(response_result.json()['code']).is_equal_to('rest_post_invalid_id')
        assert_that(response_result.json()).contains('message')
        assert_that(response_result.json()['message']).is_equal_to('Invalid post ID.')
