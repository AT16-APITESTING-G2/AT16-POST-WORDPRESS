""" Module for requests to an API
"""
from http import HTTPStatus
from json import JSONDecodeError
import os
import requests
from assertpy import assert_that
from main.core.utils.custom_logger import CustomLogger
from main.core.utils.json_reader import JsonReader
from main.core.utils.api_constants import HttpMethods
from main.trello.utils.trello_constants import ConfigurationRoute
from main.core.utils.json_decrypt import JsonDecrypt
#LOGGER=CustomLogger(__name__)

class RequestsManager:
    """ Request Manager Implementation
    """
    
    __instance None
    def __init__(self,config_file=""):
        """ Initialize request manager with a configuration file
        Parameters

	Parameters
	config_file:str,optional
   	json file with configuration needed,by default"/main/core/resources/config.json
	"""

	self._config = JsonReader.get_json('./configuration.json')
	__environment = JsonReader.get_json('./environment.json')
	env_selected = self._config.get("environment","test")
	self.env_users =_environment.get(env_selected).get("users")
	self.headers = {"Accept":_environment["headers"]}
	self.url = _environment.get(env_selected).get("api-url")
	self.key = self. _env_users.get("admin").get("key")
	self.token = self. _env_users.get("admin").get("token")
	self.response = None


    @staticmethod
    def get_instance ()
        """This method get a instance of the RequestsManager class.
        Returns:
        RequestManager -- return a instance of ReauestsManager class.
        """
        if RequestsManager.__instance is None:
            RequestsManager.__instance = RequestsManager()
            return RequestsManager.__instance
            
    def send_request (self, http_method, endpoint_route, payload=None, **kwargs):	
        """Send request
        Parameters
        http_method str
            HTTP Method
        endpoint_route : str
            Application's endpoint
        payload: Dict, option al
            Requests body, by default None
        Returns
        ----------
        response
            request response
        """
        #LOGGER.info(f"REQUEST: {http_method}, to: {self.url}{endpoint_route}")
        self.response = requests.request(
            method = HttpMethods [http_method].value,
            url = f"{self.url}{endpoint_route}",
            headers = self.headers,
            params = ("key": kwargs.get("key", self.key), "token": kwargs.get("token", self.token)), # Aut
            data = None if payload is None else payload
        )
        try:
            assert_that(self.response.status_code).\
                is_equal_to(HTTPStatus.OK.value)
            print(self.response.status_code)
            #LOGGER. info(
            #    f"==> Status Code:\"{self.response.status_code}\"")
        except Assert1ontrror as err:
            print(err)
            #LOGGER.error(f"==>{err}")
        try:
            return self.response.json(), self.response.status_code
        except JSONDecodeError:
            response_ text = {"text" : self.response.text}
            return response text, self.response.status_code
