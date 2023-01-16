import requests
import json

access_token = "INSERT TOKEN"
client_token = "INSERT TOKEN"

network_list_name = input("Enter the name of the network list to search: ")

headers = {
    "Authorization": f"EG1-HMAC-SHA256 client_token={client_token};access_token={access_token}",
    "Content-Type": "application/json"
}

response = requests.get("https://MODIFYURL.luna.akamaiapis.net/network-list/v2/network-lists", headers=headers)

if response.status_code != 200:
    print(f"Error: Failed to get the list of network lists. Status code: {response.status_code} Message: {response.text}")
    exit(1)

network_lists = response.json()

network_list = None
for nl in network_lists["networkLists"]:
    if nl["name"] == network_list_name:
        network_list = nl
        break

if network_list is None:
    print(f"Error: Failed to find network list {network_list_name}")
    exit(1)

response = requests.get(f"https://MODIFYURL.luna.akamaiapis.net/config-secure-provisioning/v1/network-lists/{network_list['id']}/configurations", headers=headers)

if response.status_code != 200:
    print(f"Error: Failed to get the list of security configurations that use network list {network_list_name}. Status code: {response.status_code} Message: {response.text}")
    exit(1)

configurations = response.json()

print(f"Security configurations that use network list {network_list_name}:")
for config in configurations["configurations"]:
    print(config["name"])
