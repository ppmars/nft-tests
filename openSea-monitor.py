import matplotlib
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import OpenSea

collection_name = "boredapeyachtclub"

OpS = OpenSea.OpenSea()
collection = OpS.getCollection(collection_name)
collection_assets = OpS.getAssets(1, 0, asset_contract=collection.ERC721Address)

for ape in collection_assets:
    # print(ape.token_id, ape.current_price)
    buyOrder = ape.buy("0xjhjdjfg")
    print(buyOrder)