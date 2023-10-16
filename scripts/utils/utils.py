import os
import yaml
import pprint
import logging

# Collection of universal helper functions for the scripts

pp = pprint.PrettyPrinter(indent=4)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ComponentAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        return f"[{self.extra['component']}] {msg}", kwargs
    
def create_logger(logger_name, component_name, log_file):
    logger = logging.getLogger(logger_name)
    component_logger = ComponentAdapter(logger, {'component': component_name})

    root_logger = logging.getLogger()
    if not root_logger.handlers:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        root_logger.addHandler(file_handler)

    return component_logger

log_file = 'logfile.log'
main_logger = create_logger(__name__, 'main', log_file)
config_logger = create_logger(__name__, 'config', log_file)
ades_logger = create_logger(__name__, 'ades', log_file)
rc_logger = create_logger(__name__, 'resource_catalogue', log_file)
das_logger = create_logger(__name__, 'data_access_services', log_file)
ls_logger = create_logger(__name__, 'login_service', log_file)
ws_logger = create_logger(__name__, 'workspace', log_file)

def load_config():
    '''
    Function to load config file
    If custom config is not present in the root directory
    uses the default values (from deployment guide)
    '''
    
    global config, base_domain, base_url, platform_domain, user_name, user_password

    current_dir = os.path.dirname(os.path.abspath(__file__))

    config_path = os.path.join(current_dir, '..', 'config', 'default_config.yaml')

    logger = logging.getLogger(__name__)
    component_logger = ComponentAdapter(logger, {'component': 'config_setup'})

    component_logger.info("Loading config file")
    
    if os.path.isfile('custom_config.yaml'):
        config_file = open('custom_config.yaml', 'r')
        config = yaml.safe_load(config_file)

        component_logger.info("CUSTOM CONFIG LOADED")
        config_file.close()
    else:
        config_file = open(config_path, 'r')
        config = yaml.safe_load(config_file)

        component_logger.info("DEFAULT CONFIG LOADED")
        config_file.close()

    base_domain = config['base_domain']
    base_url = config['base_url']
    platform_domain = config['platform_domain']
    user_name = config['USER_NAME']
    user_password = config['USER_PASSWORD']

    return config if isinstance(config, dict) else dict(config)

config = load_config()

def setup_urls(base_domain, user_name):

    ades_base_url = "http://ades-open." + base_domain
    ades_wps_url = ades_base_url + "/" + user_name + "/zoo"
    ades_proc_url = ades_base_url + "/" + "_run/wps3"

    return ades_proc_url, ades_wps_url

