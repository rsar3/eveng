import requests
import json

# Replace these with your server details

ISE_SERVER = 'http://10.150.1.14:9060'
USERNAME = 'admin'
PASSWORD = 'Vmware@12345'

def get_endpoints():
    url = f"{ISE_SERVER}/ers/config/endpoint"

    # Use HTTP Basic Authentication
    response = requests.get(url, auth=(USERNAME, PASSWORD), verify=False)

    # Check the response
    if response.status_code == 200:
        endpoints = json.loads(response.text)
        return endpoints
    else:
        print(f"Error: {response.status_code}")
        return None

endpoints = get_endpoints()
if endpoints:
    print(endpoints)

