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
from crud_post import CrudPost


class DeletePost:

    def test_delete_post(self):

        url = config('URL')
        id_post = config('ID_POST')
        token = config('TOKEN')
        crud_post = CrudPost()
        response = crud_post.delete_post(url, token, id_post)
        response_str_void = crud_post.delete_post(url, token, " ")
        assert_that(response.status_code).is_equal_to(http.HTTPStatus.OK)
        assert_that(response_str_void.status_code).is_equal_to(http.HTTPStatus.NOT_FOUND)

