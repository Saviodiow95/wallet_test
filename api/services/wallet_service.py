from django.db.models import Sum
from django.http import Http404

from api.services import application_service, rescue_service
from financial.models import Wallet


def wallet_list(user):
    wallet, created = Wallet.objects.get_or_create(owner=user)
    return wallet


def wallet_list_id(id):
    try:
        return Wallet.objects.get(id=id)
    except Wallet.DoesNotExist:
        raise Http404


def wallet_balance_asset(asset, wallet):
    applcations_amount = application_service.list_application_asset(asset=asset, wallet=wallet).aggregate(balance=Sum('amount')).get('balance')
    rescues_amount = rescue_service.list_rescue_asset(asset=asset, wallet=wallet).aggregate(balance=Sum('amount')).get('balance')
    if rescues_amount:
        return applcations_amount-rescues_amount
    return applcations_amount
