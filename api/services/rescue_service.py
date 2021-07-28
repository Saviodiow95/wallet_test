
from api.services import wallet_service
from api.utils.custom_exception import InsufficientFundsException
from financial.models import Rescue


def list_rescue(user):
    """

    :param user:
    :return:
    """
    return Rescue.objects.filter(wallet__owner=user)


def list_rescue_asset(asset, wallet):
    """

    :param asset:
    :param wallet:
    :return:
    """
    return Rescue.objects.filter(asset=asset, wallet=wallet)


def create_rescue(rescue):
    """

    :param rescue:
    :return:
    """
    balance = wallet_service.wallet_balance_asset(asset=rescue.asset, wallet=rescue.wallet)
    if balance >= rescue.amount:
        return Rescue.objects.create(wallet=rescue.wallet, asset=rescue.asset, amount=rescue.amount,
                                     price_unit=rescue.price_unit, ip_access=rescue.ip_access)

    raise InsufficientFundsException
