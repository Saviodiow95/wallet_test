import json

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from api.serializers.asset_serializer import AssetSerializer
from financial.models import Asset


class ApiTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='teste', password='teste')
        self.client = Client()
        self.client.force_login(self.user, backend=None)
        Asset.objects.create(name='Bitcoin', modality='cp', price=150.00)
        Asset.objects.create(name='Doge', modality='cp', price=59.00)
        Asset.objects.create(name='CDB', modality='rf', price=150.00)
        Asset.objects.create(name='Ação Petrobras', modality='cv', price=27.79)

    def test_asset_list(self):
        """Testando se a lista retornada pela api é igual ao retorno do Banco"""
        # obtendo os ativos pela api
        response = self.client.get(reverse('asset_list'))
        # obtendo os ativos pelo ORM
        assets = Asset.objects.all()
        serializer = AssetSerializer(assets, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_asset_list_id(self):
        """Testando se o ativo retornado pela api é igual ao retorno do Banco"""
        # obtendo os ativos pela api
        response = self.client.get('/api/asset/1')
        # obtendo os ativos pelo ORM
        assets = Asset.objects.get(pk=1)
        serializer = AssetSerializer(assets, many=False)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_asset_create(self):
        asset_valid = {
            "name": "Bitcoin",
            "modality": "cp",
            "price": 200.00
        }
        asset_invalid = {
            "name": "",
            "modality": "cp",
            "price": 200.00
        }

        response_valid = self.client.post(reverse('asset_list'),
                                          data=json.dumps(asset_valid),
                                          content_type='application/json')
        self.assertEqual(response_valid.status_code, status.HTTP_201_CREATED)

        response_invalid = self.client.post(reverse('asset_list'),
                                            data=json.dumps(asset_invalid),
                                            content_type='application/json')
        self.assertEqual(response_invalid.status_code, status.HTTP_400_BAD_REQUEST)

    def test_asset_update(self):
        asset = {
            "id": 1,
            "name": "Bitcoin",
            "modality": "cp",
            "price": 200.00
        }

        response = self.client.put('/api/asset/1',
                                   data=json.dumps(asset),
                                   content_type='application/json')
        # Teste de retorno do status_code
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Teste se o retorno da api, etá de acordo com os dados enviados
        serializer = AssetSerializer(asset, many=False)
        self.assertEqual(response.data, serializer.data)
