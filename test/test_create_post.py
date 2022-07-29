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
from model.crud_post import CrudPost
from decouple import config
from model.login import Login


def setup_module():
    global TOKEN

    TOKEN = Login().get_token()


def test_create_post():

    url = config('URL')
    content = config('CONTENT')
    page = config('PAGE')
    author = config('AUTHOR')
    status = config('STATUS')
    title = config('TITLE')

    crud_post = CrudPost(TOKEN)
    response = crud_post.create_post(url, title, content, page, status, author)
    response_text = json.loads(response.text)

    assert_that(response.status_code).is_equal_to(http.HTTPStatus.CREATED)


def test_create_post_with_a_valid_id():

    url = config('URL')
    content = config('CONTENT')
    page = config('PAGE')
    author = config('AUTHOR')
    status = config('STATUS')
    title = config('TITLE')

    crud_post = CrudPost(TOKEN)
    response = crud_post.create_post(url, title, content, page, status, author)
    response_text = json.loads(response.text)

    assert_that(response.status_code).is_equal_to(http.HTTPStatus.CREATED)
    assert_that(response_text['id']).is_instance_of(int)

def test_create_post_with_a_publish_status():

    url = config('URL')
    content = config('CONTENT')
    page = config('PAGE')
    author = config('AUTHOR')
    status = config('STATUS')
    title = config('TITLE')

    crud_post = CrudPost(TOKEN)
    response = crud_post.create_post(url, title, content, page, status, author)
    response_text = json.loads(response.text)

    assert_that(response.status_code).is_equal_to(http.HTTPStatus.CREATED)
    assert_that(response_text['status']).is_equal_to("publish")

def test_create_post_with_standard_format_by_default():

    url = config('URL')
    content = config('CONTENT')
    page = config('PAGE')
    author = config('AUTHOR')
    status = config('STATUS')
    title = config('TITLE')

    crud_post = CrudPost(TOKEN)
    response = crud_post.create_post(url, title, content, page, status, author)
    response_text = json.loads(response.text)

    assert_that(response_text['format']).is_equal_to("standard")



def test_create_post_with_void_title():

    url = config('URL')
    content = config('CONTENT')
    page = config('PAGE')
    author = config('AUTHOR')
    status = config('STATUS')
    title = ''

    crud_post = CrudPost(TOKEN)
    response = crud_post.create_post(url, title, content, page, status, author)
    response_text = json.loads(response.text)

    assert_that(response.status_code).is_equal_to(http.HTTPStatus.CREATED)
    assert_that(response_text['title']['raw']).is_empty()
    assert_that(response_text['title']['raw']).is_not_equal_to('Created post 1')

def test_create_post_with_void_status():

    url = config('URL')
    content = config('CONTENT')
    page = config('PAGE')
    author = config('AUTHOR')
    status = ''
    title = config('TITLE')

    crud_post = CrudPost(TOKEN)
    response = crud_post.create_post(url, title, content, page, status, author)
    response_text = json.loads(response.text)

    assert_that(response.status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
    assert_that(response_text['data']['details']['status']['code']).is_equal_to('rest_not_in_enum')
    assert_that(response_text['data']['details']['status']['data']).is_equal_to(None)

def test_create_post_with_invalid_author_id():

    url = config('URL')
    content = config('CONTENT')
    page = config('PAGE')
    author = config('INVALID_AUTHOR')
    status = 'publish'
    title = config('TITLE')

    crud_post = CrudPost(TOKEN)
    response = crud_post.create_post(url, title, content, page, status, author)
    response_text = json.loads(response.text)

    assert_that(response.status_code).is_equal_to(http.HTTPStatus.BAD_REQUEST)
    assert_that(response_text['code']).is_equal_to('rest_invalid_author')
    assert_that(response_text['message']).is_equal_to('Invalid author ID.')
