from brownie import MockV3Aggregator, FundMe, network, config
from scripts.helpful_scripts import (
    get_account,
    deploy_mock,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def main():
    deploy_fund_me()


def deploy_fund_me():
    account = get_account()
    # pass the price feed address to our fundMe contract

    # if we are on LIVE blockchain that can check ether price
    # else deploy mock
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mock()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    return fund_me
