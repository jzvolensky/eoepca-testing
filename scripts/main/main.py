import importlib
import yaml
import sys

sys.path.append("./scripts/utils/")
sys.path.append("./scripts/processing/")

from ades import List_Processes
from helpscripts import Load_Config, Setup_Urls

def Run_Selected_Modules(selected_modules):
    for module_name in selected_modules:
        try:
            module = importlib.import_module(module_name)
            Load_Config()
            Setup_Urls(base_domain, user_name)
        except ImportError:
            print(f"Error: Module '{module_name}' not found.")


def main():
    try:
        with open("config.yaml", "r") as yaml_file:
            config = yaml.safe_load(yaml_file)
            selected_components = config.get("components", [])
            
            
            component_to_module = {
                "resource_catalogue": "resource_catalogue",
                "ades": "ades",  
            }
            
            # Create a list of module names based on selected components
            selected_modules = [component_to_module[component] for component in selected_components]
            
            Run_Selected_Modules(selected_modules)
    except FileNotFoundError:
        print("Error: Configuration file 'config.yaml' not found.")
    except Exception as e:
        print(f"Error: {str(e)}")