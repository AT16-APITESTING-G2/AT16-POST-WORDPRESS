""" Module for requests to an API
"""
from http import HTTPStatus
from json import JSONDecodeError
import os
import requests
from assertpy import assert_that
#from main.core.utils.custom_logger import CustomLogger
from core.utils.Loggers import Logger
from core.utils.json_reader import JsonReader
from core.utils.api_constants import HttpMethods
from model.utils.word_press_constants import ConfigurationRoute
#from main.core.utils.json_decrypt import JsonDecrypt


# LOGGER=CustomLogger(__name__)

class RequestsManager:
    """ Request Manager Implementation
    """

    __instance = None

    def __init__(self, config_file=""):
        """ Initialize request manager with a configuration file
        """

        self.__config = JsonReader.get_json("./configuration.json")
        __environment = JsonReader.get_json("./environment.json")
        env_selected = self.__config.get("environment", "test")
        self.__env_users = __environment.get(env_selected).get("users")
        self.headers = __environment["headers"]
        self.url = __environment.get(env_selected).get("api-url")
        self.response = None
        self.loggers = Logger(10)

    @staticmethod
    def get_instance():
        """This method get a instance of the RequestsManager class.
        Returns:
        RequestManager -- return a instance of ReauestsManager class.
        """
        if RequestsManager.__instance is None:
            RequestsManager.__instance = RequestsManager()
            return RequestsManager.__instance

    def send_request(self, http_method, endpoint_route, payload=None, params={}):
        """Send request
        """
        self.loggers.info(f"REQUEST: {http_method}, to: {self.url}{endpoint_route}")
        self.response = requests.request(
            method=HttpMethods[http_method].value,
            url=f"{self.url}{endpoint_route}",
            headers=self.headers,
            params=params,
            data=payload
        )
        try:
            assert_that(self.response.status_code). \
                is_equal_to(HTTPStatus.GONE.value)
            self.loggers.info(f"==> Status Code:\"{self.response.status_code}\"")
        except AssertionError as err:
            print(err)
            self.loggers.error(f"==>{err}")
        try:
            return self.response.json(), self.response.status_code
        except JSONDecodeError:
            response_text = {"text": self.response.text}
            return response_text, self.response.status_code