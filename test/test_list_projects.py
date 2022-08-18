from pprint import pprint

from core.request_manager import RequestsManager
from core.utils.api_constants import HttpMethods
from model.utils.word_press_constants import ConfigurationRoute



def test_list_projects():
    response = RequestsManager.get_instance().send_request(
            HttpMethods.GET.value,
            ConfigurationRoute.GET_PROJECTS.value,
        )
    pprint(response)