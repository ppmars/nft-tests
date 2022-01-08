import OpenSea
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
plt.style.use('ggplot')

# collection name is the only input
collection_name = "veefriends"

OpS = OpenSea.OpenSea()
collection = OpS.get_collection(collection_name)
events = OpS.get_events(1200, asset_contract_address=collection.ERC721Address, event_type="successful")

# y
sale_prices = [float(event.total_price) / 1000000000000000000 for event in events]
# x
dates = [datetime.strptime(event.created_date, "%Y-%m-%dT%H:%M:%S.%f") for event in events]
# x must be integers for np.polyfit()
x = range(len(sale_prices))

plt.scatter(x, sale_prices)
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, sale_prices, 1))(np.unique(x)), color="blue")
plt.title("Last {} {} Sales".format(len(x), collection_name))
plt.ylabel("Eth")
plt.show()


# for ape in OpenSea.get_assets(name=collection_name):
#     # print(ape.token_id, ape.current_price)
#     buyOrder = ape.buy("0xjhjdjfg")
#     print(buyOrder)