from financial.models import Application


def list_application(user):
    """

    :param user:
    :return:
    """
    return Application.objects.filter(wallet__owner=user)


def list_application_asset(asset, wallet):
    """

    :param asset:
    :param wallet:
    :return:
    """
    return Application.objects.filter(asset=asset, wallet=wallet)


def create_application(application):
    """

    :param application:
    :return: Application
    """
    return Application.objects.create(
        wallet=application.wallet,
        asset=application.asset,
        amount=application.amount,
        price_unit=application.price_unit, ip_access=application.ip_access
    )
