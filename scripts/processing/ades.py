import requests
import pprint
from utils.helpscripts import Load_Config, Setup_Urls


pp = pprint.PrettyPrinter(indent=4)

def List_Processes(ades_proc_url):
    '''
    Function to make API calls to ades to get list of avilable processes
    '''
    try:
        response = requests.get(ades_proc_url)
        print(f'1. URL from the List processes functions: {ades_proc_url}')
        if response.status_code == 200:
            print("ADES API call successful")
            response_json = response.json()
            print("ADES processes retrieved:")
            pp.pprint(response_json)
        else:
            print("ADES API call failed")
    except requests.exceptions.RequestException as e:
        print(e)
    
    try:
        response2 = requests.get(ades_proc_url + "/processes")
        print(f'2. URL from the List processes functions: {ades_proc_url}')
        if response2.status_code == 200:
            print("ADES API call successful")
            response_json = response2.json()
            print("ADES processes retrieved:")
            pp.pprint(response_json)
        else:
            print("ADES API call failed")
    except requests.exceptions.RequestException as e:
        print(e)

    return response_json

if __name__ == "__main__":
    config, base_domain, base_url, platform_domain, user_name, user_password = Load_Config()
    ades_proc_url, ades_wps_url = Setup_Urls(base_domain, user_name)
    List_Processes(ades_proc_url)