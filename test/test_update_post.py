#
# @test_update_post.py Copyright (c) 2022 Jalasoft
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
from assertpy.assertpy import assert_that
from model.crud_post import CrudPost
from decouple import config

from model.login import Login


def setup_module():
    global TOKEN

    TOKEN = Login().get_token()


def test_update_post():

    TITLE = config('TITLE')
    CONTENT = config('CONTENT')

    URL = config('URL')
    ID_POST = config('ID_POST')

    crud_post = CrudPost(TOKEN)
    response = crud_post.update_post(URL, TITLE, CONTENT, ID_POST)
    assert_that(response.status_code).is_equal_to(HTTPStatus.OK)
