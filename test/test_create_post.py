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

import http
import json
from assertpy import assert_that
from crud_post import CrudPost
from decouple import config
from helpers.login import Login


class TestCreatePost:

    def test_create_post(self):

        URI_TOKEN = config('URI_TOKEN')
        USER_NAME = config('USER_NAME')
        PASSWORD = config('PASSWORD')

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

        response_login = Login().login(URI_TOKEN, USER_NAME, PASSWORD).json()
        token = response_login['token_type'] + ' ' + response_login['jwt_token']

        crud_post = CrudPost()
        response = crud_post.create_post(url, token, title, content, page, status)
        response_text = json.loads(response.text)
        assert_that(response.status_code).is_equal_to(http.HTTPStatus.CREATED)
        assert_that(response_text['id']).is_instance_of(int)
        assert_that(response.json()['id']).is_instance_of(int)
        assert_that(response.json()['author']).is_instance_of(int)
        assert_that(response.json()).contains("modified")
        assert_that(response.json()).contains("status")
        assert_that(response.json()['format']).is_equal_to("standard")
