#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author github.com/L1ghtM4n

__all__ = ['networks', 'handlers']

# Import modules
from requests import get

# Networks which supported by pywallet module
networks = ['BTC', 'ETH', 'LTC', 'DASH', 'DOGE']

# blockcypher balance api handler
def __blockcypher(address: str, coin: str) -> int:
    endpoint = 'https://api.blockcypher.com/v1/{coin}/main/addrs/{address}/balance'.format(
        coin=coin.lower(),
        address=address
    )
    response = get(endpoint).json()
    return response['final_balance']

# Handlers for balance
handlers = [
    { 
        "coins": ['BTC', 'ETH', 'DASH', 'DOGE', 'LTC'],
        "handler": __blockcypher
    }
]