import requests
import pprint
import os
import sys

relative_paths = ["../utils", "../processing", "../resource_catalogue"]
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.extend(os.path.join(current_dir, rel_path) for rel_path in relative_paths)

from utils import ades_logger

def List_Processes(ades_proc_url):
    '''
    Function to make API calls to ades to get list of avilable processes
    '''

    try:
        response = requests.get(ades_proc_url)
        if response.status_code == 200:
            ades_logger.info("ADES API call successful")
            response_json = response.json()
            ades_logger.info("ADES processes retrieved successfully")
        else:
            ades_logger.error("ADES API call failed")
    except requests.exceptions.RequestException as e:
        print(e)
    
    return response_json

