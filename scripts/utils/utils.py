import os
import yaml
import pprint
import logging

# Collection of universal helper functions for the scripts

pp = pprint.PrettyPrinter(indent=4)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def Load_Config():
    '''
    Function to load config file
    If custom config is not present in the root directory
    uses the default values (from deployment guide)

    '''
    current_dir = os.path.dirname(os.path.abspath(__file__))

    config_path = os.path.join(current_dir, '..', 'config', 'default_config.yaml')

    logging.info("Loading config file")
    
    if os.path.isfile('custom_config.yaml'):
        config_file = open('custom_config.yaml', 'r')
        config = yaml.safe_load(config_file)

        logging.info("CUSTOM CONFIG LOADED")
        config_file.close()
    else:
        config_file = open(config_path, 'r')
        config = yaml.safe_load(config_file)

        logging.info("DEFAULT CONFIG LOADED")
        config_file.close()

    base_domain = config['base_domain']
    base_url = config['base_url']
    platform_domain = config['platform_domain']
    user_name = config['USER_NAME']
    user_password = config['USER_PASSWORD']
    
    return config, base_domain, base_url, platform_domain, user_name, user_password

def Setup_Urls(base_domain, user_name):

    ades_base_url = "http://ades-open." + base_domain
    ades_wps_url = ades_base_url + "/" + user_name + "/zoo"
    ades_proc_url = ades_base_url + "/" + "_run/wps3"

    logging.info(f'ADES processes URL: {ades_proc_url}')
    logging.info(f'ADES WPS URL: {ades_wps_url}')
    

    return ades_proc_url, ades_wps_url