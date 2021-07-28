from django.http import Http404

from financial.models import Asset


def list_assets():
    """
    Retorna uma lista com todos os ativos cadastrados no banco
    :return: List(Asset)
    """
    return Asset.objects.all()


def create_asset(asset):
    """
    Cria um novo ativo recebendo uma entidade Asset como parâmetro
    :param asset:
    :return: Asset
    """
    return Asset.objects.create(name=asset.name, modality=asset.modality, price=asset.price)


def list_asset_id(pk):
    """
    Busca um ativo de acordo  com seu id, em casos que o id informado
    não pertença nenhum ativo ele retornara uma exceção Http404
    :param pk: id do Asset desejado
    :type pk: int
    :return :Asset ou Http404
    """
    try:
        return Asset.objects.get(id=pk)
    except Asset.DoesNotExist:
        raise Http404


def list_asset_wallet(waller):
    """
    Busca os ativos de acordo com a aplicações que possuem este ativo,
    filtrando as aplicações pela carteira
    :param waller:
    :type waller: Waller
    :return: list(Asset)
    """
    return Asset.objects.filter(application__wallet=waller)


def list_asset_modality(modality):
    """
    Lista todos os ativos de acordo com a modalidade informada
    :param modality:
    :return: List(Asset)
    """
    return Asset.objects.filter(modality=modality)

def edit_asset(asset_old, asset_new):
    asset_old.name = asset_new.name
    asset_old.modality = asset_new.modality
    asset_old.price = asset_new.price
    asset_old.save(force_update=True)
