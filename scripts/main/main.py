import importlib
import yaml
import sys
import os
import logging

# TODO:Find a way to make this better and more streamlined
relative_paths = ["../utils", "../processing", "../resource_catalogue", "../component_actions"]
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.extend(os.path.join(current_dir, rel_path) for rel_path in relative_paths)

from ades import List_Processes
from utils import Load_Config, Setup_Urls
from component_actions import component_actions


def main():
    config = Load_Config()
    
    selected_components = config.get("components", [])
    
    for component in selected_components:
        if component in component_actions:
            action_function = component_actions[component]
            action_function()
        else:
            logging.warning(f"No action defined for component: {component}")

        
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    main()