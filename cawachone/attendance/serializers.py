from rest_framework import serializers

from asset.serializers import AssetSerializers
from .models import AttendanceSheet, DailyReport


# from .v import DailyReport


class MonthlySheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceSheet
        fields = '__all__'


class DialyReportSerializer(serializers.ModelSerializer):
    tagId = AssetSerializers()

    class Meta:
        model = DailyReport
        fields = ['tagId', 'lastSeen', 'inTime']
