# Large Tether Transfer Agent

## Description

This agent detects large mint and burns of stETH for the lido project

## Supported Chains

- Ethereum

## Alerts
Following is an example alert for the bot:
```
1 findings for transaction 0x518c1fe65e0bf7fb2365e9080ef505b0561409e409ed15dcff4f0352cd36bb4d {
  "name": "Large stETh Mint",
  "description": "26.903787861071276 stEth minted",
  "alertId": "FORTA-7",
  "protocol": "Lido",
  "severity": "Info",
  "type": "Info",
  "metadata": {
    "to": "0x13020547534Fb51ffF373Ae0Ac9F85C36408A81B",
    "amount": 26.903787861071276
  },
  "addresses": [],
  "labels": [],
  "uniqueKey": "",
  "source": {},
  "timestamp": "2024-04-23 17:08:44.923450"
}
```
## Test Data

The agent behaviour can be verified with the following transactions:

- 0x518c1fe65e0bf7fb2365e9080ef505b0561409e409ed15dcff4f0352cd36bb4d (Mint 26 stETH)
