import requests
from assertpy.assertpy import assert_that
import json

from utils.print_helpers import pretty_print

url = "http://localhost/wordpress/wordpress/wp-json/api/v1/token?mo_rest_api_test_config=jwt_auth"

payload={'username': 'dayler',
'password': '123'}
files=[

]
headers = {}

def test_delete_post():

    response = requests.delete(url , payload, files)
    print(response.json())
    posts = response.json()
    print(posts)
    assert_that(response.status_code).is_equal_to(201)
