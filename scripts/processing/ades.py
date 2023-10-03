import requests
import pprint
import os
import sys
import logging

# Get the path to the current directory (main_folder)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the paths to the 'utils', 'processing', and 'resource_catalogue' folders to sys.path
utils_path = os.path.join(current_dir, "../utils")
processing_path = os.path.join(current_dir, "../processing")
resource_catalogue_path = os.path.join(current_dir, "../resource_catalogue")

sys.path.append(utils_path)
sys.path.append(processing_path)
sys.path.append(resource_catalogue_path)

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