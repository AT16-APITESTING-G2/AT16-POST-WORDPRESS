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
from assertpy import assert_that
from crud_post import CrudPost
from decouple import config
from helpers.login import Login


class TestCreatePost:

    def test_create_post(self):

        url = config('URL')
        content = config('CONTENT')
        page = config('PAGE')
        author = config('AUTHOR')
        status = config('STATUS')
        title = config('TITLE')
        uri_token = config('URI_TOKEN')
        username = config('USER_NAME')
        password = config('PASSWORD')

        response_login = Login().login(uri_token, username, password).json()
        token = response_login['token_type'] + ' ' + response_login['jwt_token']

        crud_post = CrudPost()
        response = crud_post.create_post(url, token, title, content, page, status, author)
        response_text = json.loads(response.text)
        assert_that(response.status_code).is_equal_to(http.HTTPStatus.CREATED)
        assert_that(response_text['id']).is_instance_of(int)
        assert_that(response_text['id']).is_instance_of(int)
        assert_that(response_text['author']).is_instance_of(int)
        assert_that(response_text['type']).is_equal_to("post")
        assert_that(response_text['status']).is_equal_to("publish")
        assert_that(response_text['format']).is_equal_to("standard")
        assert_that(response_text['title']['raw']).is_equal_to('Created post 1')

    def test_create_post_with_void_title(self):

        url = config('URL')
        content = config('CONTENT')
        page = config('PAGE')
        author = config('AUTHOR')
        status = config('STATUS')
        title = ''
        uri_token = config('URI_TOKEN')
        username = config('USER_NAME')
        password = config('PASSWORD')

        response_login = Login().login(uri_token, username, password).json()
        token = response_login['token_type'] + ' ' + response_login['jwt_token']

        crud_post = CrudPost()
        response = crud_post.create_post(url, token, title, content, page, status, author)
        response_text = json.loads(response.text)

        assert_that(response.status_code).is_equal_to(http.HTTPStatus.CREATED)
        assert_that(response_text['title']['raw']).is_empty()
        assert_that(response_text['title']['raw']).is_not_equal_to('Created post 1')

    def test_create_post_with_void_status(self):

        url = config('URL')
        content = config('CONTENT')
        page = config('PAGE')
        author = config('AUTHOR')
        status = ''
        title = config('TITLE')
        uri_token = config('URI_TOKEN')
        username = config('USER_NAME')
        password = config('PASSWORD')

        response_login = Login().login(uri_token, username, password).json()
        token = response_login['token_type'] + ' ' + response_login['jwt_token']

        crud_post = CrudPost()
        response = crud_post.create_post(url, token, title, content, page, status, author)
        response_text = json.loads(response.text)

        assert_that(response.status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
        assert_that(response_text['data']['details']['status']['code']).is_equal_to('rest_not_in_enum')
        assert_that(response_text['data']['details']['status']['data']).is_equal_to(None)

    def test_create_post_with_invalid_author_id(self):

        url = config('URL')
        content = config('CONTENT')
        page = config('PAGE')
        author = config('INVALID_AUTHOR')
        status = 'publish'
        title = config('TITLE')
        uri_token = config('URI_TOKEN')
        username = config('USER_NAME')
        password = config('PASSWORD')

        response_login = Login().login(uri_token, username, password).json()
        token = response_login['token_type'] + ' ' + response_login['jwt_token']

        crud_post = CrudPost()
        response = crud_post.create_post(url, token, title, content, page, status, author)
        response_text = json.loads(response.text)

        assert_that(response.status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
        assert_that(response_text['code']).is_equal_to('rest_invalid_author')
        assert_that(response_text['message']).is_equal_to('Invalid author ID.')
