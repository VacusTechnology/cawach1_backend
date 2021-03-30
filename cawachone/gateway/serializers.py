from rest_framework import serializers

from .models import Gateway


class GatewaySerializers(serializers.ModelSerializer):
    class Meta:
        model = Gateway
        fields = '__all__'
