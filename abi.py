import json
from dotenv import load_dotenv
import os

load_dotenv()
# fetches a contract's abi from etherscan using its address
def fetch_abi(address):
    import requests

    url = 'https://api.etherscan.io/api'
    etherscan_api_key = os.environ.get("ETHERSCAN_API_KEY")

    params = {
        "module": "contract",
        "action": "getabi",
        "address": address,
        "apikey": etherscan_api_key
    }

    response = requests.request("GET", url, params=params)
    # print(response.json()['result'])
    return response.json()['result']