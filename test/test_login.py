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

import pytest
import allure
from http import HTTPStatus
from assertpy import assert_that, soft_assertions
from decouple import config
from model.login import Login


@allure.severity("blocker")
@allure.suite("sanity_testing")
@allure.suite("regression_testing")
@allure.suite("smoke_testing")
@allure.suite("acceptance_testing")
@allure.epic("sanity_testing")
@allure.epic("regression_testing")
@allure.epic("smoke_testing")
@allure.epic("acceptance_testing")
@allure.title("Login test case")
@allure.step("Login test case")
@allure.description("This test case is used to verify that user login was succesfull")
def test_login_success():
    URL = config('URI_TOKEN')
    USER_NAME = config('USER_NAME')
    PASSWORD = config('PASSWORD')

    user_login = Login()

    response_login = user_login.login(URL, USER_NAME, PASSWORD)

    with soft_assertions():
        assert_that(response_login.status_code).is_equal_to(HTTPStatus.OK)

    assert_that(response_login.json()).contains("token_type")
    assert_that(response_login.json()['token_type']).is_equal_to('Bearer')
    allure.attach(response_login.json()['token_type'], 'Token type', allure.attachment_type.TEXT)
    assert_that(response_login.json()).contains("iat")
    allure.attach(str(response_login.json()['iat']), 'iat', allure.attachment_type.TEXT)
    assert_that(response_login.json()['iat']).is_instance_of(int)
    assert_that(response_login.json()).contains("expires_in")
    allure.attach(str(response_login.json()['expires_in']), 'Expires in', allure.attachment_type.TEXT)
    assert_that(response_login.json()['expires_in']).is_instance_of(int)
    assert_that(response_login.json()).contains("jwt_token")
    allure.attach(response_login.json()['jwt_token'], 'Jwt token', allure.attachment_type.TEXT)
    assert_that(response_login.json()['jwt_token']).is_not_empty()


@allure.severity("blocker")
@allure.suite("sanity_testing")
@allure.suite("regression_testing")
@allure.suite("smoke_testing")
@allure.suite("negative_testing")
@allure.epic("sanity_testing")
@allure.epic("regression_testing")
@allure.epic("smoke_testing")
@allure.epic("negative_testing")
@allure.title("Login test case with a bad user name")
@allure.step("Login test case with a bad user name")
@allure.description("This test case is used to verify that user cannot login with a bad user name")
def test_login_with_bad_user_name():
    URL = config('URI_TOKEN')
    USER_NAME = config('USER_NAME')
    PASSWORD = config('PASSWORD')

    user_login = Login()

    response_login = user_login.login(URL, "BAD_USER_NAME", PASSWORD)

    assert_that(response_login.status_code).is_equal_to(HTTPStatus.BAD_REQUEST)


@allure.severity("blocker")
@allure.suite("sanity_testing")
@allure.suite("regression_testing")
@allure.suite("smoke_testing")
@allure.suite("negative_testing")
@allure.epic("sanity_testing")
@allure.epic("regression_testing")
@allure.epic("smoke_testing")
@allure.epic("negative_testing")
@allure.title("Login test case with a bad password")
@allure.step("Login test case with a bad password")
@allure.description("This test case is used to verify that user cannot login with a bad password")
def test_login_with_bad_password():
    URL = config('URI_TOKEN')
    USER_NAME = config('USER_NAME')
    PASSWORD = config('PASSWORD')

    user_login = Login()

    response_login = user_login.login(URL, USER_NAME, "BAD_PASSWORD")

    assert_that(response_login.status_code).is_equal_to(HTTPStatus.BAD_REQUEST)
