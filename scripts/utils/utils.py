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

logger = logging.getLogger(__name__)
config_logger = ComponentAdapter(logger, {'component': 'config'})
ades_logger = ComponentAdapter(logger, {'component': 'ades'})
rc_logger = ComponentAdapter(logger, {'component': 'resource_catalogue'})


def Load_Config():
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

config = Load_Config()

def Setup_Urls(base_domain, user_name):

    ades_base_url = "http://ades-open." + base_domain
    ades_wps_url = ades_base_url + "/" + user_name + "/zoo"
    ades_proc_url = ades_base_url + "/" + "_run/wps3"

    return ades_proc_url, ades_wps_url

