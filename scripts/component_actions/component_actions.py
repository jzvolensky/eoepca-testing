import sys
import os
import logging

relative_paths = ["../utils", "../processing", "../resource_catalogue", "../component_actions"]
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.extend(os.path.join(current_dir, rel_path) for rel_path in relative_paths)

from ades import list_processes
from resource_catalogue import list_records
from workspace import example_ws_function
from login_service import example_ls_function
from data_access_services import example_das_function

from utils import load_config, setup_urls, config


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_ades_tests():
    logging.info("Running ADES tests...")
    base_domain = config['base_domain']
    user_name = config['USER_NAME']
    ades_proc_url, ades_wps_url = setup_urls(base_domain, user_name)
    list_processes(ades_proc_url)

    

def run_resource_catalogue_tests():
    logging.info("Running Resource Catalogue tests...")
    base_domain = config['base_domain']
    list_records()

def run_workspace_tests():
    logging.info("Running Workspace tests...")
    example_ws_function()

def run_login_service_tests():
    logging.info("Running Login Service tests...")
    example_ls_function()

def run_data_access_services_tests():
    logging.info("Running Data Access Services tests...")
    example_das_function()

component_actions = {
    "ades": run_ades_tests,
    "resource_catalogue": run_resource_catalogue_tests,
    "workspace": run_workspace_tests,
    "login_service": run_login_service_tests,
    "data_access_services": run_data_access_services_tests
}