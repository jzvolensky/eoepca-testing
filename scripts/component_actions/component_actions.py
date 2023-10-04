import sys
import os
import logging

relative_paths = ["../utils", "../processing", "../resource_catalogue", "../component_actions"]
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.extend(os.path.join(current_dir, rel_path) for rel_path in relative_paths)

from ades import List_Processes
from resource_catalogue import List_Records
from utils import Load_Config, Setup_Urls, config


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def Run_Ades_Tests():
    logging.info("Running ADES tests...")
    base_domain = config['base_domain']
    user_name = config['USER_NAME']
    ades_proc_url, _ = Setup_Urls(base_domain, user_name)
    List_Processes(ades_proc_url)
    

def Run_Resource_Catalogue_Tests():
    logging.info("Running Resource Catalogue tests...")
    base_domain = config['base_domain']
    List_Records()

component_actions = {
    "ades": Run_Ades_Tests,
    "resource_catalogue": Run_Resource_Catalogue_Tests,
}