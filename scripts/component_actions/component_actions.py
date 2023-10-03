import sys
import os
import logging
from ades import List_Processes
from utils import Load_Config, Setup_Urls

# TODO:Find a way to make this better and more streamlined
current_dir = os.path.dirname(os.path.abspath(__file__))

utils_path = os.path.join(current_dir, "../utils")
processing_path = os.path.join(current_dir, "../processing")
resource_catalogue_path = os.path.join(current_dir, "../resource_catalogue")

sys.path.append(utils_path)
sys.path.append(processing_path)
sys.path.append(resource_catalogue_path)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')



def Run_Ades_Tests():
    config, base_domain, base_url, platform_domain, user_name, user_password = Load_Config()
    ades_proc_url, _ = Setup_Urls(base_domain, user_name)
    List_Processes(ades_proc_url)
    logging.info("Running ADES tests")

def Run_Resource_Catalogue_Tests():
    logging.info("Running Resource Catalogue tests")

component_actions = {
    "ades": Run_Ades_Tests,
    "resource_catalogue": Run_Resource_Catalogue_Tests,
}