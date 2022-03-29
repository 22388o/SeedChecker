#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author github.com/L1ghtM4n

__all__ = ['main']

# Import modules
from rich import print
from rich.prompt import Prompt
from rich.progress import track
from pywallet import wallet
# Import packages
from core.handlers import handlers, networks

def main() -> int:
    # Request seed phrase
    seed = Prompt.ask("[bold cyan][?][/bold cyan] Please enter seed phrase")
    # Generate wallets from seed phrase in supported networks
    wallets = [wallet.create_wallet(network=network, seed=seed, children=1) for network in networks]
    # Progress bar
    for wallet_index in track(range(len(wallets)), description=f"[bold green]Scanning {len(wallets)} blockchains[/bold green]"):
        # Fetch address and coin from wallet object
        address, coin = wallets[wallet_index]['address'], wallets[wallet_index]['coin']
        # Find balance api handler for coin
        found_handlers = list(filter(lambda h: coin in h['coins'], handlers))
        # Show balance
        if found_handlers:
            balance = found_handlers[0]['handler'](address=address, coin=coin)
            print('\n[bold green]Coin [yellow]{coin}[/yellow]\n\tAddress: [white]{address}[/white]\n\tBalance: [white]{balance}[/white]\n[/bold green]'.format(
                coin=coin,
                address=address,
                balance=balance,
            ))
    return 0

if __name__ == '__main__':
    exit(main())
