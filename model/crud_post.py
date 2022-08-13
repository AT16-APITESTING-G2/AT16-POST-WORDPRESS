#
# @crud_post.py Copyright (c) 2022 Jalasoft
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

from core.api_request import APIRequest


class CrudPost:

    def __init__(self, token):
        self.headers = {
            'Authorization': token
        }
        self.params = {
            'mo_rest_api_test_config': 'jwt_auth'
        }

    def create_post(self, url, payload):

        response = APIRequest().request("POST", url, self.headers, self.params, payload)
        return response

    def delete_post(self, URL, id_post):
        url = "{}/{}".format(URL, id_post)

        response = APIRequest().request("DELETE", url, self.headers, self.params)

        return response

    def retrieve_post(self, url, id_post):

        new_url = "{}/{}".format(url, id_post)

        response = APIRequest().request("GET", new_url, self.headers, self.params)
        return response

    def update_post(self, url, id, payload):
        new_url = "{}/{}".format(url, id)
        response = APIRequest().request("POST", new_url, self.headers, self.params, payload)
        return response
