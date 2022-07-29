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
from decouple import config
import json
from assertpy import assert_that
from model.crud_post import CrudPost
from model.login import Login


def setup_module():
    global TOKEN

    TOKEN = Login().get_token()


def test_delete_post_statusok():

    url = config('URL')
    id_post = config('ID_POST')
    crud_post = CrudPost(TOKEN)

    response = crud_post.delete_post(url, id_post)
    assert_that(response.status_code).is_equal_to(http.HTTPStatus.OK)

def test_delete_post_status_void():

    url = config('URL')
    crud_post = CrudPost(TOKEN)

    response_str_void = crud_post.delete_post(url, " ")
    assert_that(response_str_void.status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)

def test_delete_post_status_invalid_id():
    url = config('URL')
    id_post = config('ID_POST')
    crud_post = CrudPost(TOKEN)
    comment_status = config('COMMENT_STATUS')

    response = crud_post.update_post(url, id_post, comment_status)
    response_text = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
    assert_that(response_text).contains('code')
    assert_that(response_text['code']).is_equal_to("rest_post_invalid_id")
