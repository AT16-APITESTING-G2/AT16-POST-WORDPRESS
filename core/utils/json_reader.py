"""Module for reading Json files
"""
import os
import json
#from main.core.utils.custom_logger import CustomLogger

#logger=CustomLogger(__name__)

class JsonReader:
    """ JsonReader Implementation
    """
    @staticmethod
    def get_json(config_file="/main/core/resources/config_sample.json"):
        """ Method to get configuration from a json file
        Parameters
        -------
            config_file:json
                Json configuration file
        Returns
        -------
            Dict
                Configuration dictionary
        """
        location_file = os.getcwd()
        location_file += f"{config_file}"

        with open(location_file) as json_file:
            try:
                configuration = json.load(json_file)
            except json.JSONDecodeError as err:
                #logger.error(f"{err}while decoding json file:\"{config_file}\"")
                raise err
        return configuration


    def __str__(self):
        pass