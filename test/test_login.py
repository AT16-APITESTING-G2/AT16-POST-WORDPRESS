# @test_login.py Copyright (c) 2022 Jalasoft
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
from decouple import config
from model.login import Login


class TestLogin(TestCase):
    def test_login_success(self):
        URL = config('URI_TOKEN')
        USER_NAME = config('USER_NAME')
        PASSWORD = config('PASSWORD')

        user_login = Login()

        response_login = user_login.login(URL, USER_NAME, PASSWORD)

        with soft_assertions():
            assert_that(response_login.status_code).is_equal_to(HTTPStatus.OK)

        assert_that(response_login.json()).contains("token_type")
        assert_that(response_login.json()['token_type']).is_equal_to('Bearer')
        assert_that(response_login.json()).contains("iat")
        assert_that(response_login.json()['iat']).is_instance_of(int)
        assert_that(response_login.json()).contains("expires_in")
        assert_that(response_login.json()['expires_in']).is_instance_of(int)
        assert_that(response_login.json()).contains("jwt_token")
        assert_that(response_login.json()['jwt_token']).is_not_empty()
