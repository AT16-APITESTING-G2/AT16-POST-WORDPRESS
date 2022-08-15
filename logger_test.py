import json
import logging

def load_json_expected_result(path):

    with open(path) as file_json:
        file_json_dict = json.load(file_json)
    return file_json_dict

#-----logging.response_text['loglevel']
response_text = load_json_expected_result("enviroment.json")
print(response_text)

logging.basicConfig(level=logging.response_text['loglevel'], filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.debug("Verify the response is 200 when a post is update succesfully")
logging.warning("Verify the response is 200 when a post is update succesfully")
logging.info("Verify the response is 200 when a post is update succesfully")

#print(level=response_text['loglevel'])