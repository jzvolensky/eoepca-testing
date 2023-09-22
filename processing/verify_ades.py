import owslib
import json
from owslib.csw import CatalogueServiceWeb
import os
import sys
import requests
import boto3
import yaml

current_dir = os.path.dirname(os.path.abspath(__file__))

# Assuming verify_ades_config.yaml is in the same directory as the script
config_file_path = os.path.join(current_dir, "verify_ades_config.yaml")

# Now you can open the config file
with open(config_file_path, 'r') as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

base_domain = config['base_domain']
platform_domain = config['platform_domain']
base_url = config['base_url']
USER_NAME = config['USER_NAME']
USER_PASSWORD = config['USER_PASSWORD']
S3_ENDPOINT = config['S3_ENDPOINT']

print(f"Configuration loaded successfuly, \n Base domain: {base_domain}, \n Base url: {base_url}")

from utils import DemoClient as client

demo = client.DemoClient(base_url)
demo.register_client()
demo.save_state()
print("demo client registered")


# ADES service URLs
ades_base_url = "http://ades-open." + base_domain
ades_wps_url = ades_base_url + "/" + USER_NAME + "/zoo"; print("ADES WPS endpoint:", ades_wps_url)
ades_proc_url = ades_base_url + "/" + USER_NAME + "/wps3"; print("ADES API Processes endpoint:", ades_proc_url)
print(ades_wps_url)
print(ades_proc_url)
print("ADES urls retrieved")

ades_access_token = None
app_name = "s-expression-0_0_2"

print(f"Using app name {app_name} , and access token {ades_access_token}")

# Testing requests to the ADES server using the requests library

url = ades_proc_url + "/processes"
print(url)
headers= {
    'authorization': f'Bearer {ades_access_token}',
    'Accept': 'application/json',
}

response = requests.get(url, headers=headers, verify=False)

if response.status_code == 200:
    # Successful response, parse and work with the JSON data if needed
    data = response.json()
    print(data)
else:
    print(f"Request failed with status code {response.status_code}")