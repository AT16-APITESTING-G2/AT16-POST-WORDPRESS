from unittest import TestCase

from assertpy.assertpy import assert_that

from crud_post import CrudPost


class TestCreatePost(TestCase):
    def test_create_post(self):
        url = ""
        token = ""
        content = ""
        page = ""
        status = ""
        title = ""

        crud_post = CrudPost()
        crud_post.create_post(url, token, title, content, page, status)
        assert_that()

