from rest_framework import serializers

from attendance.models import AttendanceSheet
from .models import ContactTracing


class ContactTracingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactTracing
        fields = '__all__'
