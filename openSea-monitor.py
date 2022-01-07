import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime
from web3 import Web3

import numpy as np

plt.style.use('ggplot')
import OpenSea

collection_name = "boredapeyachtclub"
collection_contract_address = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"

OpS = OpenSea.OpenSea()
# collection = OpS.getCollection(collection_name)
# collection_assets = OpS.getAssets(1, 0, asset_contract=collection.ERC721Address)
#
# for ape in collection_assets:
#     # print(ape.token_id, ape.current_price)
#     buyOrder = ape.buy("0xjhjdjfg")
#     print(buyOrder)

events = OpS.get_events(300, asset_contract_address=collection_contract_address, event_type="successful")
print("got " + str(len(events)) + " events")
sale_prices = []
dates = []
for event in events:
    print(event.jsonData)
    dates.append(datetime.strptime(event.created_date, "%Y-%m-%dT%H:%M:%S.%f"))
    sale_prices.append(float(event.total_price))
sale_prices = [x / 1000000000000000000 for x in sale_prices]

x = range(len(sale_prices))
plt.scatter(x, sale_prices)
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, sale_prices, 1))(np.unique(x)), color="blue")
plt.show()
