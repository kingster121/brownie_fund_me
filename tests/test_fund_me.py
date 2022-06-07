from scripts.helpful_scripts import get_account
from scripts.deploy import deploy_fund_me


def test():
    account = get_account()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee()

    tx1 = fund_me.fund({"from": account, "value": entrance_fee})
    tx1.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee

    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == 0