import owslib
import json
from owslib.csw import CatalogueServiceWeb
import os
import sys
import requests
import boto3
import yaml
import pprint

pp = pprint.PrettyPrinter(indent=4)
# Load config file
# If custom_config.txt is not present in root
# Use default_config.yaml in scripts/config/
def Load_Config():
    '''
    Function to load config file
    If custom config is not present in the root directory
    uses the default values (from deployment guide)

    '''
    current_dir = os.path.dirname(os.path.abspath(__file__))

    config_path = os.path.join(current_dir, '..', 'config', 'default_config.yaml')

    

    print('LOADING CONFIG')
    if os.path.isfile('custom_config.yaml'):
        config_file = open('custom_config.yaml', 'r')
        config = yaml.safe_load(config_file)
        print(f'CUSTOM CONFIG LOADED: {config}')
        config_file.close()
    else:
        config_file = open(config_path, 'r')
        config = yaml.safe_load(config_file)
        print('DEFAULT CONFIG LOADED')
        pp.pprint(config)
        config_file.close()

    base_domain = config['base_domain']
    base_url = config['base_url']
    platform_domain = config['platform_domain']
    user_name = config['USER_NAME']
    user_password = config['USER_PASSWORD']
    
    return config, base_domain, base_url, platform_domain, user_name, user_password

def Setup_Urls(base_domain, user_name):

    ades_base_url = "http://ades-open." + base_domain
    ades_wps_url = ades_base_url + "/" + user_name + "/zoo"; print("ADES WPS endpoint:", ades_wps_url)
    ades_proc_url = ades_base_url + "/" + "_run/wps3"; print("ADES API Processes endpoint:", ades_proc_url)
    print(ades_wps_url)
    print(ades_proc_url)
    print("ADES urls retrieved")

    return ades_proc_url, ades_wps_url


def List_Processes(ades_proc_url):
    '''
    Function to make API calls to ades to get list of avilable processes
    '''
    try:
        response = requests.get(ades_proc_url)
        print(f'1. URL from the List processes functions: {ades_proc_url}')
        if response.status_code == 200:
            print("ADES API call successful")
            response_json = response.json()
            print("ADES processes retrieved:")
            pp.pprint(response_json)
        else:
            print("ADES API call failed")
    except requests.exceptions.RequestException as e:
        print(e)
    
    try:
        response2 = requests.get(ades_proc_url + "/processes")
        print(f'2. URL from the List processes functions: {ades_proc_url}')
        if response2.status_code == 200:
            print("ADES API call successful")
            response_json = response2.json()
            print("ADES processes retrieved:")
            pp.pprint(response_json)
        else:
            print("ADES API call failed")
    except requests.exceptions.RequestException as e:
        print(e)

    return response_json
