import importlib
import yaml
import sys
import os
import logging

# TODO:Find a way to make this better and more streamlined
current_dir = os.path.dirname(os.path.abspath(__file__))

utils_path = os.path.join(current_dir, "../utils")
processing_path = os.path.join(current_dir, "../processing")
resource_catalogue_path = os.path.join(current_dir, "../resource_catalogue")

sys.path.append(utils_path)
sys.path.append(processing_path)
sys.path.append(resource_catalogue_path)

from ades import List_Processes
from utils import Load_Config, Setup_Urls

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    config, base_domain, base_url, platform_domain, user_name, user_password = Load_Config()
    
    selected_components = config.get("components", [])
    logging.info(f"Selected components: {selected_components}")
    
    for component in selected_components:
        if component == "ades":
            logging.info("Running ADES tests...")
            ades_proc_url, _ = Setup_Urls(base_domain, user_name)
            List_Processes(ades_proc_url)
        elif component == "resource_catalogue":
            logging.info("Running Resource Catalogue tests...")
        

if __name__ == "__main__":
    main()