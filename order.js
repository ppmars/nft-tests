import Web3 from "web3"
import { OpenSeaPort, Network } from 'opensea-js'
import {OrderSide} from "opensea-js/lib/types.js";

// This example provider won't let you make transactions, only read-only calls:
const infura_key = "540fd91b69a844b595f70bd064188a22"
const provider = new Web3.providers.HttpProvider("https://mainnet.infura.io/v3/"+infura_key)

const seaport = new OpenSeaPort(provider, {
    networkName: Network.Main,
    apiKey: process.env.OPENSEA_API_KEY
})

const order = await seaport.api.getOrder({
    side:
    OrderSide.Sell,
    asset_contract_address: "address",
    token_id: 0
})

const accountAddress = "0" // The buyer's wallet address, also the taker
const transactionHash = await this.props.seaport.fulfillOrder({ order, accountAddress })
function getTransactionHash(transactionHash) {
    return transactionHash
}
getTransactionHash(transactionHash)