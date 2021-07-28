from rest_framework import serializers

from financial.models import Rescue


class RescueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rescue
        fields = ('id', 'wallet', 'asset', 'amount', 'price_unit', 'date', 'ip_access')
