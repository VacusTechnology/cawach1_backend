from django.contrib import admin

# Register your models here.
from attendance.models import DailyReport, AttendanceSheet

admin.site.register(DailyReport)
admin.site.register(AttendanceSheet)