from rest_framework import serializers

from financial.models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'wallet', 'asset', 'amount', 'price_unit', 'date', 'ip_access')
