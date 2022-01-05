import Web3 from "web3"
const accounts = await ethereum.request({ method: 'eth_accounts' });

try {
  const transactionHash = await ethereum.request({
    method: 'eth_sendTransaction',
    params: [
      {
        to: "0xB0BFa3Db3D777EFf4d1C7a10995c04aDc2803d9d",
        from: accounts[0],
        value: '0x01',
        // And so on...
      },
    ],
  });
  // Handle the result
  console.log(transactionHash);
} catch (error) {
  console.error(error);
}
