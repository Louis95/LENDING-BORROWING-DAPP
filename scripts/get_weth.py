
from scripts.utilities import get_account
from brownie import interface, config,network

def main():
    get_weth()


def get_weth():
    """
    Mint weth by depositing ETH.
    """

    account = get_account()
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    tx = weth.deposit({"from": account, "value": 0.1 * 10 ** 18})
    print(f"We just received 0.1 weth")
    tx.wait(1)
    return tx