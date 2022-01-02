from web3 import Web3
import json
import abi

EIP20_ABI = json.loads('[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint8"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_from","type":"address"},{"indexed":true,"name":"_to","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"_owner","type":"address"},{"indexed":true,"name":"_spender","type":"address"},{"indexed":false,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]')  # noqa: 501

ganache_url = 'HTTP://127.0.0.1:8545'
web3 = Web3(Web3.HTTPProvider(ganache_url))

account_1 = '0x54001a54Cf32C9DF537152124e8314544F348423'
account_2 = '0x6C8aa32498F155bc24471ff578b52f79F1a3e0E5'
private_key = '0xcb57c2e6749a1c57a4498e13930a2908fb923dccda7df8407baa81dbe65f6dd8'
nonce = web3.eth.getTransactionCount(account_1)

tx = {
    "nonce": nonce,
    "to": account_2,
    "value": web3.toWei(1, 'ether'),
    "gas": 5000000,
    "gasPrice": 20000000000
}

# signed_tx = web3.eth.account.signTransaction(tx, private_key)
# tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
# print(web3.toHex(tx_hash))
mainnet_bayc_address = "0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D"
ganache_bayc_address = "0xABE5A777d895F105205D5BB3a095fd630607e17b"

bored_apes = web3.eth.contract(address=ganache_bayc_address, abi=abi.fetch_abi(mainnet_bayc_address))
mint_ape_tx = bored_apes.functions.mintApe(1).buildTransaction({
     # 'chainId': 1,
     'gas': 5000000,
     'maxFeePerGas': web3.toWei('2', 'gwei'),
     'maxPriorityFeePerGas': web3.toWei('1', 'gwei'),
     'nonce': nonce,
 })
print(mint_ape_tx)
signed_tx = web3.eth.account.signTransaction(mint_ape_tx, private_key)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))