from web3 import Web3
import abi

ganache_url_development = 'HTTP://127.0.0.1:7545'
ganache_url_development7 = 'HTTP://127.0.0.1:8545'
web3 = Web3(Web3.HTTPProvider(ganache_url_development7))

account_1 = '0x54444A128A251dF44cb53f3E3617562523824Fb4'
account_2 = '0x1853189E496eabd013BAD1C9FBF834895F4A90bc'
private_key_1 = '0xfa4b20bbe7426aa5f48dd8d10c08200abe008b6c8c3b07a4f4f70662387e05a5'
private_key_2 = '0x218b06e199d348314db6951916483623ca6037aec642ecda1fbe2011df6dc4d3'

# tx = {
#     "nonce": nonce,
#     "to": account_2,
#     "value": web3.toWei(1, 'ether'),
#     "gas": 5000000,
#     "gasPrice": 20000000000
# }
#
# signed_tx = web3.eth.account.signTransaction(tx, private_key)
# tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
# print(web3.toHex(tx_hash))
mainnet_bayc_address = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"
ganache_bayc_address = "0x7287F635F2f60bc7238DB9470487017E7A2d8B23"

bored_apes = web3.eth.contract(address=ganache_bayc_address, abi=abi.fetch_abi(mainnet_bayc_address))

# enable sale
nonce = web3.eth.getTransactionCount(account_1)
flip_sale_tx = bored_apes.functions.flipSaleState().buildTransaction({
     'maxFeePerGas': web3.toWei('2', 'gwei'),
     'maxPriorityFeePerGas': web3.toWei('1', 'gwei'),
     'nonce': nonce,
     'from': web3.toChecksumAddress(account_1),
 })
signed_tx = web3.eth.account.signTransaction(flip_sale_tx, private_key_1)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

nonce = web3.eth.getTransactionCount(account_2)
mint_ape_tx = bored_apes.functions.mintApe(1).buildTransaction({
     'value': web3.toWei('0.08', 'ether'),
     'maxFeePerGas': web3.toWei('2', 'gwei'),
     'maxPriorityFeePerGas': web3.toWei('1', 'gwei'),
     'nonce': nonce,
     'from': web3.toChecksumAddress(account_2),
 })

print("raw tx: {}".format(mint_ape_tx))
signed_tx = web3.eth.account.signTransaction(mint_ape_tx, private_key_2)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print("mint successful, tx hash: {}".format(web3.toHex(tx_hash)))