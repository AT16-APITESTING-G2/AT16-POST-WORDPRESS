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

from utils.request import APIRequest

class CrudPost:

    def create_post(self, url, token, title, content, page, status, author):

        payload = {'title': title,
                   'content': content,
                   'page': page,
                   'status': status,
                   'author': author}

        headers = {
            'Authorization': token
        }

        response = APIRequest().post(url, payload, headers)
        return response

    def delete_post(self, URL, token, id_post):
        url = URL + id_post

        headers = {
            'Authorization': token
        }
        response = APIRequest().delete(url, headers)

        print(response.text)
        return response

    def retrieve_post(self, url, token, id_post):

        new_url = url + id_post
        headers = {
            'Authorization': token
        }
        response = APIRequest().get(new_url, headers)
        return response

    def update_post(self, url, token, title, content, id_post):
        new_url = url + id_post

        payload = {'title': title,
                   'content': content}

        headers = {'Authorization': token}
        response = APIRequest().post(new_url, payload, headers)
        return response
        