#
# @login.py Copyright (c) 2022 Jalasoft
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


class Login:

    def login(self, url, user, password):
        _url = url
        headers = {}
        payload = {
            'username': user,
            'password': password
        }

        response = requests.post(url, data=payload, headers=headers)

        return response
