#
# @api_request.py Copyright (c) 2022 Jalasoft
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

from dataclasses import dataclass
import requests


@dataclass
class Response:
    status_code: int
    text: str
    as_dict: object
    headers: dict


class APIRequest:

    def get(self, url, headers):
        response = requests.get(url, headers=headers)
        return self.__get_responses(response)

    def post(self, url, payload, headers):
        response = requests.post(url, data=payload, headers=headers)
        return self.__get_responses(response)

    def delete(self, url, headers):
        response = requests.delete(url, headers=headers)
        return self.__get_responses(response)

    def __get_responses(self, response):
        status_code = response.status_code
        text = response.text
        try:
            as_dict = response.json()
        except Exception:
            as_dict = {}
        headers = response.headers
        return Response(status_code, text, as_dict, headers)
