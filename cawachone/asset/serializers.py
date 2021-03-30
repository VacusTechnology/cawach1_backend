from rest_framework import serializers

from .models import AssetHealth


class AssetSerializers(serializers.Serializer):
    studentName = serializers.CharField(max_length=50)
    tagId = serializers.CharField(max_length=30)
    registrationNo = serializers.CharField(max_length=20)
    department = serializers.CharField(max_length=30)
    phoneNumber = serializers.CharField(max_length=15)
    mailId = serializers.CharField(max_length=50)
    gender = serializers.CharField(max_length=10)


class AssetHealthSerializers(serializers.ModelSerializer):
    asset = AssetSerializers()

    class Meta:
        model = AssetHealth
        fields = ['asset', 'lastseen', 'battery']
