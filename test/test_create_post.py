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
from assertpy import assert_that, soft_assertions
from crud_post import CrudPost
from decouple import config

from helpers.login import Login


class TestCreatePost(TestCase):
    def test_create_post(self):
        url = config('URL')
        content = config('CONTENT')
        page = config('PAGE')
        status = config('STATUS')
        title = config('TITLE')
        uri_token = config('URI_TOKEN')
        username = config('USER_NAME')
        password = config('PASSWORD')

        response_login = Login().login(uri_token, username, password).json()

        token = response_login['token_type'] + ' ' + response_login['jwt_token']

        crud_post = CrudPost()
        response = crud_post.create_post(url, token, title, content, page, status)

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(HTTPStatus.CREATED)
        assert_that(response.json()['id']).is_instance_of(int)
        assert_that(response.json()['author']).is_instance_of(int)
        assert_that(response.json()).contains("modified")
        assert_that(response.json()).contains("status")
        assert_that(response.json()['format']).is_equal_to("standard")

    def test_verify_non_void_title(self):
        url = config('URL')
        content = config('CONTENT')
        page = config('PAGE')
        status = config('STATUS')
        title = ''
        uri_token = config('URI_TOKEN')
        username = config('USER_NAME')
        password = config('PASSWORD')

        response_login = Login().login(uri_token, username, password).json()

        token = response_login['token_type'] + ' ' + response_login['jwt_token']

        crud_post = CrudPost()
        response = crud_post.create_post(url, token, title, content, page, status)

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(HTTPStatus.CREATED)
        assert_that(response.json()['title'['response']]).is_equal_to(HTTPStatus.CREATED)
