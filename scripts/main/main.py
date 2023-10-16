import sys
import os
import logging

relative_paths = ["../utils", "../processing", "../resource_catalogue","../workspace", "../login_service", "../data_access_services", "../component_actions"]
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.extend(os.path.join(current_dir, rel_path) for rel_path in relative_paths)

from utils import load_config
from component_actions import component_actions
from utils import config, main_logger

def main():
    
    selected_components = config.get("components", [])

    main_logger.info(f"Running tests for components: {selected_components}")
    
    for component in selected_components:
        if component in component_actions:
            action_function = component_actions[component]
            action_function()
        else:
            logging.warning(f"No action defined for component: {component}")

        

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    main()