from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from api.serializers.wallet_serializer import WalletSerializer
from financial.models import Wallet, Asset, Application, Rescue


class ApiTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='teste', password='teste')
        self.client = Client()
        self.client.force_login(self.user, backend=None)
        self.wallet = Wallet.objects.create(owner=self.user)
        self.asset = Asset.objects.create(name='Bitcoin', modality='cp', price=150.00)

    def test_wallet_list(self):
        """Testando se a carteira retornada pela api é igual ao retorno do Banco"""
        # obtendo os ativos pela api
        response = self.client.get(reverse('wallet_list'))
        # obtendo os ativos pelo ORM
        wallet = Wallet.objects.get(owner=self.user)
        serializer = WalletSerializer(wallet, many=False)
        self.assertEqual(response.data, serializer.data)

    def test_wallet_balance(self):
        """
        Testes para saber se o valor do saldo da carteira esta retornando correto
        """
        # realiza uma aplicação
        Application.objects.create(wallet=self.wallet, asset=self.asset, amount=10, price_unit=150.00)
        response = self.client.get(reverse('wallet_list'))
        # compara o saldo da carteira retornado pela API com o retornado pelo ORM
        self.assertTrue(self.wallet.balance() == response.data['balance'])

        Rescue.objects.create(wallet=self.wallet, asset=self.asset, amount=4, price_unit=140.00)
        # compara o saldo da carteira retornado pela API com o retornado pelo ORM apos a realização de um resgate
        self.assertTrue(self.wallet.balance() != response.data['balance'])

        # atualiza o retorno do banco e compara o saldo da carteira retornado pela API com o retornado pelo ORM
        response = self.client.get(reverse('wallet_list'))
        self.assertTrue(self.wallet.balance() == response.data['balance'])
