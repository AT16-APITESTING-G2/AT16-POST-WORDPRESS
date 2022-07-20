from http import HTTPStatus
from unittest import TestCase
from assertpy import assert_that
from crud_post import CrudPost
from decouple import config


class RetrieveTestPost(TestCase):

    def test_retrieve_post(self):
        URL = config('URL')
        ID_POST = config('ID_POST')
        TOKEN = config('TOKEN')

        crud_post = CrudPost()
        response_result = crud_post.retrieve_post(URL, TOKEN, ID_POST)

        assert_that(response_result.status_code).is_equal_to(HTTPStatus.OK)
