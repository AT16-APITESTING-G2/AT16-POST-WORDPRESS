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

from utils.api_request import APIRequest


class CrudPost:

    def __init__(self, token):
        self.headers = {
            'Authorization': token
        }

    def create_post(self, url, title, content, page, status, author):

        payload = {'title': title,
                   'content': content,
                   'page': page,
                   'status': status,
                   'author': author}

        response = APIRequest().post(url, payload, self.headers)
        return response

    def delete_post(self, URL, id_post):
        url = URL + id_post

        response = APIRequest().delete(url, self.headers)

        print(response.text)
        return response

    def retrieve_post(self, url, id_post):

        new_url = url + id_post

        response = APIRequest().get(new_url, self.headers)
        return response

    def update_post(self, url, title, content, id_post):
        new_url = url + id_post

        payload = {'title': title,
                   'content': content}

        response = APIRequest().post(new_url, payload, self.headers)
        return response
        