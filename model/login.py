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
from decouple import config
from core.request_manager import RequestsManager
from core.utils.api_constants import HttpMethods
from model.utils.word_press_constants import ConfigurationRoute
class Login:

    def login(self, user, password):
        data = {
            'username': user,
            'password': password
        }

        return RequestsManager.get_instance().send_request(
            HttpMethods.POST.value,
            ConfigurationRoute.TOKEN.value,
            data
        )

    def get_token(self):

        USER_NAME = config('USER_NAME')
        PASSWORD = config('PASSWORD')

        response_login = self.login(USER_NAME, PASSWORD).json()

        TOKEN = response_login['token_type'] + ' ' + response_login['jwt_token']

        return TOKEN