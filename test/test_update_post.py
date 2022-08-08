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

import json
import allure
import pytest
from http import HTTPStatus
from assertpy.assertpy import assert_that
from model.crud_post import CrudPost
from decouple import config
from model.login import Login
from test.test_create_post import load_json_expected_result


@pytest.fixture(autouse=True)
def setup_prerequisites():
    global TOKEN
    global ID_POST

    URL = config("URL")
    payload = load_json_expected_result("resources/resource_retrieve_test/payload_create_post.json")
    TOKEN = Login().get_token()
    crud_post = CrudPost(TOKEN)

    api_request_response = json.loads((crud_post.create_post(URL, payload)).text)
    ID_POST = api_request_response['id']
    yield
    crud_post.delete_post(URL, ID_POST)


@pytest.mark.acceptance_testing
@pytest.mark.smoke_testing
@pytest.mark.regression_testing
@allure.severity("critical")
@allure.suite("smoke_testing")
@allure.suite("regression_testing")
@allure.suite("acceptance_testing")
@allure.epic("smoke_testing")
@allure.epic("regression_testing")
@allure.epic("acceptance_testing")
@allure.link('https://apitestpost16.atlassian.net/browse/AP-20', name="Verify the response is 200 when a post is update "
                                                                      "successfully")
@allure.title("Update post test")
@allure.step("Update an existing Post")
@allure.description("This test case is used to update an existing post")
def test_update_post():
    url = config('URL')
    crud_post = CrudPost(TOKEN)
    allure.attach(url, 'URL', allure.attachment_type.TEXT)
    payload = load_json_expected_result("resources/resource_update_test/payload_update_post.json")
    response = crud_post.update_post(url, ID_POST, payload)
    response_text = json.loads(response.text)
    allure.attach(json.dumps(response_text, indent=4), 'JSON Response', allure.attachment_type.JSON)
    assert_that(response.status_code).is_equal_to(HTTPStatus.OK)
    allure.attach(str(response.status_code), 'Status code return', allure.attachment_type.TEXT)
    assert_that(response_text).contains('id')
    allure.attach(str(response_text['id']), 'Post id:', allure.attachment_type.TEXT)
    assert_that(response_text['id']).is_instance_of(int)


@pytest.mark.functional_testing
@pytest.mark.regression_testing
@allure.severity("minor")
@allure.suite("functional_testing")
@allure.suite("regression_testing")
@allure.epic("functional_testing")
@allure.epic("regression_testing")
@allure.link('https://apitestpost16.atlassian.net/browse/AP-32', name="Verify the response is 200 when the author’s "
                                                                      "post is update successfully")
@allure.title("Update post author field")
@allure.step("Update post author field")
@allure.description("This test case is used to update the author field of an existing post")
def test_update_post_author_field():
    url = config('URL')

    crud_post = CrudPost(TOKEN)
    payload = load_json_expected_result("resources/resource_update_test/payload_update_author_post.json")
    response = crud_post.update_post(url, ID_POST, payload)
    response_text = json.loads(response.text)
    allure.attach(json.dumps(response_text, indent=4), 'JSON Response:', allure.attachment_type.JSON)
    assert_that(response.status_code).is_equal_to(HTTPStatus.OK)
    allure.attach(str(response.status_code), 'Status code return:', allure.attachment_type.TEXT)
    assert_that(response_text).contains('author')
    allure.attach(str(response_text['author']), 'Author id:', allure.attachment_type.TEXT)
    assert_that(response_text['author']).is_instance_of(int)


@pytest.mark.functional_testing
@pytest.mark.regression_testing
@allure.severity("minor")
@allure.suite("functional_testing")
@allure.suite("regression_testing")
@allure.epic("functional_testing")
@allure.epic("regression_testing")
@allure.link('https://apitestpost16.atlassian.net/browse/AP-33', name="Verify the response is 200 when the status' post "
                                                                      "is update successfully")
@allure.title("Update post status field")
@allure.step("Update post status field")
@allure.description("This test case is used to update the status field of an existing post")
def test_update_status_post_field():
    url = config('URL')

    crud_post = CrudPost(TOKEN)
    payload = load_json_expected_result("resources/resource_update_test/payload_update_status_post.json")
    response = crud_post.update_post(url, ID_POST, payload)
    response_text = json.loads(response.text)
    allure.attach(json.dumps(response_text, indent=4), 'JSON Response:', allure.attachment_type.JSON)
    assert_that(response.status_code).is_equal_to(HTTPStatus.OK)
    allure.attach(str(response.status_code), 'Status code return:', allure.attachment_type.TEXT)
    assert_that(response_text).contains('status')
    allure.attach(str(response_text['status']), 'Post status:', allure.attachment_type.TEXT)
    assert_that(response_text['status']).is_not_empty()


@pytest.mark.functional_testing
@pytest.mark.regression_testing
@allure.severity("normal")
@allure.suite("functional_testing")
@allure.suite("regression_testing")
@allure.epic("functional_testing")
@allure.epic("regression_testing")
@allure.link('https://apitestpost16.atlassian.net/browse/AP-37', name="Verify the response is 400 and when the comment "
                                                                      "status value is different  that: open or closed")
@allure.title("Update comment status post field")
@allure.step("Update comment status post field")
@allure.description("This test case is used to update the comment status field of an existing post")
def test_update_comment_status_post():
    url = config('URL')

    crud_post = CrudPost(TOKEN)
    payload = load_json_expected_result("resources/resource_update_test/payload_update_comment_status_post.json")
    response = crud_post.update_post(url, ID_POST, payload)
    response_text = json.loads(response.text)
    allure.attach(json.dumps(response_text, indent=4), 'JSON Response:', allure.attachment_type.JSON)
    assert_that(response.status_code).is_equal_to(HTTPStatus.OK)
    allure.attach(str(response.status_code), 'Status code return:', allure.attachment_type.TEXT)
    assert_that(response_text).contains('comment_status')
    allure.attach(str(response_text['comment_status']), 'Comment status:', allure.attachment_type.TEXT)
    assert_that(response_text['comment_status']).is_not_empty()


@pytest.mark.negative_testing
@pytest.mark.regression_testing
@allure.severity("critical")
@allure.suite("negative_testing")
@allure.suite("regression_testing")
@allure.epic("negative_testing")
@allure.epic("regression_testing")
@allure.link('https://apitestpost16.atlassian.net/browse/AP-36', name="Verify the response is 400 and code content "
                                                                       "field is “rest post invalid id“ when the id "
                                                                       "used is invalid or not exists")
@allure.title("Update an existing post with an invalid id")
@allure.step("Update an existing post with an invalid id")
@allure.description("This is a negative test case that is used to update an existing post with an invalid id")
def test_update_post_with_invalid_id():
    url = config('URL')
    id = 9999999

    crud_post = CrudPost(TOKEN)
    payload = load_json_expected_result("resources/resource_update_test/payload_update_invalid_id.json")
    response = crud_post.update_post(url, id, payload)
    response_text = json.loads(response.text)
    allure.attach(json.dumps(response_text, indent=4), 'JSON Response:', allure.attachment_type.JSON)
    assert_that(response.status_code).is_equal_to(HTTPStatus.NOT_FOUND)
    allure.attach(str(response.status_code), 'Status code return:', allure.attachment_type.TEXT)
    assert_that(response_text).contains('code')
    allure.attach(str(response_text['code']), 'Response:', allure.attachment_type.TEXT)
    assert_that(response_text['code']).is_equal_to("rest_post_invalid_id")


@pytest.mark.negative_testing
@pytest.mark.regression_testing
@allure.severity("minor")
@allure.suite("negative_testing")
@allure.suite("regression_testing")
@allure.epic("negative_testing")
@allure.epic("regression_testing")
@allure.link('https://apitestpost16.atlassian.net/browse/AP-35', name="Verify the response is 400 and when the status "
                                                                      "value is different  that: publish, future, "
                                                                      "draft, pending or private")
@allure.title("Update status field post with an invalid value")
@allure.step("Update status field post with an invalid value")
@allure.description("This is a negative test case that is used to update status field of an existing post with an "
                    "invalid value. (an invalid value is different than: publish, future, draft, pending or private)")
def test_update_status_field_with_invalid_value():
    url = config('URL')

    crud_post = CrudPost(TOKEN)
    payload = load_json_expected_result("resources/resource_update_test/payload_update_invalid_status_field.json")
    response = crud_post.update_post(url, ID_POST, payload)
    response_text = json.loads(response.text)
    allure.attach(json.dumps(response_text, indent=4), 'JSON Response:', allure.attachment_type.JSON)
    assert_that(response.status_code).is_equal_to(HTTPStatus.BAD_REQUEST)
    allure.attach(str(response.status_code), 'Status code return:', allure.attachment_type.TEXT)
    assert_that(response_text).contains('code')
    allure.attach(str(response_text['code']), 'Response:', allure.attachment_type.TEXT)
    assert_that(response_text['code']).is_equal_to("rest_invalid_param")


@pytest.mark.negative_testing
@pytest.mark.regression_testing
@allure.severity("minor")
@allure.suite("negative_testing")
@allure.suite("regression_testing")
@allure.epic("negative_testing")
@allure.epic("regression_testing")
@allure.link('https://apitestpost16.atlassian.net/browse/AP-34', name="Verify the response is 200 when the comment "
                                                                       "status post is update successfully")
@allure.title("Update comment status field post with an invalid value")
@allure.step("Update comment status field post with an invalid value")
@allure.description("This is a negative test case that is used to update comment status field of an existing post with "
                    "an invalid value. (an invalid value is different than: open, closed)")
def test_update_comment_status_field_with_invalid_value():
    url = config('URL')

    crud_post = CrudPost(TOKEN)
    payload = load_json_expected_result("resources/resource_update_test/payload_update_invalid_status_field.json")
    response = crud_post.update_post(url, ID_POST, payload)
    response_text = json.loads(response.text)
    allure.attach(json.dumps(response_text, indent=4), 'JSON Response:', allure.attachment_type.JSON)
    assert_that(response.status_code).is_equal_to(HTTPStatus.BAD_REQUEST)
    allure.attach(str(response.status_code), 'Status code return:', allure.attachment_type.TEXT)
    assert_that(response_text).contains('code')
    allure.attach(str(response_text['code']), 'Response:', allure.attachment_type.TEXT)
    assert_that(response_text['code']).is_equal_to("rest_invalid_param")


@pytest.mark.negative_testing
@pytest.mark.regression_testing
@allure.severity("minor")
@allure.suite("negative_testing")
@allure.suite("regression_testing")
@allure.epic("negative_testing")
@allure.epic("regression_testing")
@allure.link('https://apitestpost16.atlassian.net/browse/AP-38', name="Verify the response is 400 and when the ping "
                                                                      "status value is different that: open or closed")
@allure.title("Update ping status field post with an invalid value")
@allure.step("Update ping status field post with an invalid value")
@allure.description("This is a negative test case that is used to update ping status field of an existing post with "
                    "an invalid value. (an invalid value is different than: open, closed)")
def test_update_invalid_ping_status_field():
    url = config('URL')

    crud_post = CrudPost(TOKEN)
    payload = load_json_expected_result("resources/resource_update_test/payload_update_invalid_ping_status_field.json")
    response = crud_post.update_post(url, ID_POST, payload)
    response_text = json.loads(response.text)
    allure.attach(json.dumps(response_text, indent=4), 'JSON Response:', allure.attachment_type.JSON)
    assert_that(response.status_code).is_equal_to(HTTPStatus.BAD_REQUEST)
    allure.attach(str(response.status_code), 'Status code return:', allure.attachment_type.TEXT)
    assert_that(response_text).contains('code')
    allure.attach(str(response_text['code']), 'Response:', allure.attachment_type.TEXT)
    assert_that(response_text['code']).is_equal_to("rest_invalid_param")
