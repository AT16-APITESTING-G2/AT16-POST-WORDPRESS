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
from assertpy import assert_that
from model.crud_post import CrudPost
from model.login import Login


def setup_module():
    global TOKEN

    TOKEN = Login().get_token()


def test_delete_post():

    url = config('URL')
    id_post = config('ID_POST')
    crud_post = CrudPost(TOKEN)

    response = crud_post.delete_post(url, id_post)
    response_str_void = crud_post.delete_post(url, " ")
    assert_that(response.status_code).is_equal_to(http.HTTPStatus.OK)
    assert_that(response_str_void.status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)

