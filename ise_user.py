import requests
from requests.auth import HTTPBasicAuth

# Replace these with your Cisco ISE details
ISE_HOST = 'https://10.150.1.14'
ERS_USER = 'admin'
ERS_PASS = 'Vmware@12345'

def get_endpoint_status(mac_address):
    """
    Get the status of an endpoint (laptop) given its MAC address.
    """
    #url = f"{ISE_HOST}/ers/config/endpoint?filter=mac.EQ.{mac_address}"
    url = f"{ISE_HOST}/ers/config/endpoint"
    response = requests.get(url, auth=HTTPBasicAuth(ERS_USER, ERS_PASS), verify=False)

    if response.status_code == 200:
        endpoint = response.json()['SearchResult']['resources'][0]
        endpoint_id = endpoint['id']
        status_url = f"{ISE_HOST}/ers/config/endpoint/{endpoint_id}"
        status_response = requests.get(status_url, auth=HTTPBasicAuth(ERS_USER, ERS_PASS), verify=False)
        status = status_response.json()['ERSEndPoint']['status']
        return status
    else:
        return None

# Test the function
mac_address = '00:00:00:00:00:00'  # Replace with your laptop's MAC address
# mac_address = '50:00:00:01:00:00'  # Replace with your laptop's MAC address
status = get_endpoint_status(mac_address)
if status:
    print(f"The laptop with MAC address {mac_address} is in {status} status.")
else:
    print("Laptop not found.")


