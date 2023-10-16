import os 
import sys

relative_paths = ["../utils", "../processing", "../resource_catalogue","../component_actions"]
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.extend(os.path.join(current_dir, rel_path) for rel_path in relative_paths)

from utils import das_logger, config

def example_das_function():
    das_logger.info("This is an example function from the data access services")