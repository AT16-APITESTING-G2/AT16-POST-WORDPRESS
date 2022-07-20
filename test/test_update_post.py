from unittest import TestCase
from assertpy.assertpy import assert_that
from crud_post import CrudPost
import os
from dotenv import load_dotenv

load_dotenv()

class TestUpdatePost(TestCase):
    def test_create_post(self):
        url = os.getenv('URL')
        token = os.getenv('TOKEN')
        content = os.getenv('CONTENT')
        title = os.getenv('TITLE')

        crud_post = CrudPost()
        response = crud_post.update_post(url, token, title, content)
        assert_that(response.status_code).is_equal_to(200)
