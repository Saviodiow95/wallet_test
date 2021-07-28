from rest_framework import serializers

from financial.models import Wallet


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('id', 'owner', 'balance', 'balance_asset')
