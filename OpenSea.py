import json

import requests


class OpenSea:
    def __init__(self):
        self.endpoints = {
            "assets": "https://api.opensea.io/api/v1/assets",
            "events": "https://api.opensea.io/api/v1/events",
            "orders": "https://api.opensea.io/wyvern/v1/orders",
            "collections": "https://api.opensea.io/collection/"
        }
        self.param_names = {
            "assets": [
                "limit",
                "offset",
                "token_ids",
                "image_url",
                "background_color",
                "name",
                "external_link",
                "asset_contract_address",
                "owner",
                "traits",
                "last_sale",
            ]
        }

    def getAssets(self, limit, offset="", token_ids="", image_url="", background_color="", name="", external_link="",
                  asset_contract="", owner="", traits="", last_sale=""):

        _params = [limit, offset, token_ids, image_url, background_color, name, external_link, asset_contract, owner,
                   traits, last_sale]
        # build request params
        params = {}
        for i, _param in enumerate(_params):
            # if the param was passed
            if _param:
                params[self.param_names["assets"][i]] = _param
        # submit request to the OpenSea api
        response = requests.request("GET", self.endpoints["assets"], params=params)
        # if response OK
        if response.status_code == 200:
            response = json.loads(response.text)
            assets = []
            for asset in response['assets']:
                assets.append(Asset(asset))
            return assets
        raise Exception(
            "[Error] request returned code {} with reason {}".format(response.status_code, response.reason))

    @staticmethod
    def getFloorPrice(collection):
        return float(collection['stats']['floor_price'])

    def getERC721Address(self, collection):
        for contract in collection['primary_asset_contracts']:
            # make sure address pertains for an ERC721 contract
            if contract["asset_contract_type"] == "non-fungible":
                return contract["address"]

    def getCollection(self, name):
        # create request url
        url = self.endpoints["collections"] + str(name)
        # submit request to the OpenSea api
        response = requests.request("GET", url)
        if response.status_code == 200:
            response = json.loads(response.text)
            return Collection(response['collection'])
        raise Exception(
            "[Error] request returned code {} with reason {}".format(response.status_code, response.reason))

class Asset:
    def __init__(self, jsonData):
        self.jsonData = jsonData
        self.token_id = jsonData['token_id']
        self.name = jsonData['name']

        if jsonData['sell_orders']:
            self.current_price = jsonData['sell_orders'][0]['current_price']
        else:
            self.current_price = None

        if jsonData["asset_contract"]["asset_contract_type"] == "non-fungible":
            self.ERC721address = jsonData["asset_contract"]["address"]

class Collection:
    def __init__(self, jsonData):
        self.jsonData = jsonData

        for contract in jsonData['primary_asset_contracts']:
            if contract["asset_contract_type"] == "non-fungible":
                self.ERC721Address = contract["address"]

        self.stats = jsonData['stats']
        self.floor = jsonData['stats']['floor_price']

# OpS = OpenSea()
# a = OpS.getAssets(2, 0)
# c = OpS.getCollection('boredapeyachtclub')
# a = OpS.getERC721Address(c)
# for asset in a:
#     print(asset.token_id)
# print(a)
