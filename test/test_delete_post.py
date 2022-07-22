import http
from decouple import config
from assertpy import assert_that
from crud_post import CrudPost



class DeletePost:

    def test_delete_post(self):
        crud_post = CrudPost()
        response = crud_post.delete_post(config('URL'), token, config('ID_POST'))
        assert_that(response.status_code).is_equal_to(http.HTTPStatus.OK)
