import requests
import pprint
import os
import sys
import logging


relative_paths = ["../utils", "../processing", "../resource_catalogue"]
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.extend(os.path.join(current_dir, rel_path) for rel_path in relative_paths)

pp = pprint.PrettyPrinter(indent=4)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def List_Processes(ades_proc_url):
    '''
    Function to make API calls to ades to get list of avilable processes
    '''
    try:
        response = requests.get(ades_proc_url)
        if response.status_code == 200:
            logging.info("ADES API call successful")
            response_json = response.json()
            logging.info("ADES processes retrieved successfully")
        else:
            logging.error("ADES API call failed")
    except requests.exceptions.RequestException as e:
        print(e)
    
    return response_json

if __name__ == "__main__":
    config, base_domain, base_url, platform_domain, user_name, user_password = Load_Config()
    ades_proc_url, ades_wps_url = Setup_Urls(base_domain, user_name)
    List_Processes(ades_proc_url)