from django.contrib.auth.models import User
from django.test import TestCase

from financial.models import Wallet, Application, Asset, Rescue


class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='teste', password='teste')
        self.wallet = Wallet.objects.create(owner=self.user)
        self.asset = Asset.objects.create(name='Bitcoin', modality='cp', price=150.00)
        Application.objects.create(wallet=self.wallet, asset=self.asset, amount=10, price_unit=150.00)

    def test_wallet_create(self):
        assert Wallet.objects.all().count() == 1

    def test_wallet_balance(self):
        """
        Testes para saber se o valor do saldo da carteira esta retornando correto
        """
        assert self.wallet.balance() == 1500.00
        asset = Asset.objects.get(pk=1)
        Rescue.objects.create(wallet=self.wallet, asset=self.asset, amount=4, price_unit=140.00)
        assert self.wallet.balance() == 900.00
        asset.price = 200
        asset.save(force_update=True)
        assert self.wallet.balance() == 1200.00
