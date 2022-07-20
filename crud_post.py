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

import requests


class CrudPost:

    def create_post(self, url, token,title, content, page, status):
        payload = {'title': title,
                   'content': content,
                   'page': page,
                   'status': status}

        headers = {
            'Authorization': token
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        return response

    def retrieve_post(self, url, token, id_post):
        new_url = url + id_post
        payload = {}
        files = {}
        headers = {
            'Authorization': token
        }

        response = requests.get(new_url, headers=headers, data=payload, files=files)
        return response

    def delete_post(self):
        return

    def update_post(self):
        return


