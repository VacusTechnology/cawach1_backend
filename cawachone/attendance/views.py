# Create your views here.
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from asset.models import Asset
from .models import AttendanceSheet, DailyReport
# from .serializers import MonthlySheetSerializer, DialyReportSerializer


class DailyReportAPI(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        try:
            attendancePayload = []
            for asset in Asset.objects.all():
                atndnce = DailyReport.objects.filter(tagId=asset)
                if atndnce.exists():
                    attendancePayload.append({"tagId": asset.tagId, "name": asset.studentName, "department": asset.department, "phoneNumber": asset.phoneNumber,
                                              "mailId": asset.mailId, "intime": atndnce[atndnce.count() - 1].inTime,
                                              "lastseen": atndnce[atndnce.count() - 1].lastSeen})
                else:
                    attendancePayload.append({"tagId": asset.tagId, "name": asset.studentName, "department": asset.department, "phonenumber": asset.phoneNumber,
                                              "mailId": asset.mailId, "intime": None, "lastseen": None})

            return Response({"attendance": attendancePayload}, status=status.HTTP_200_OK)

        except Exception as err:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class MonthlySheetApi(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        try:
            attendancePayload = []
            for asset in Asset.objects.all():
                monthlyattendance = AttendanceSheet.objects.filter(tagId=asset)
                if monthlyattendance.exists():
                    attendancePayload.append({"tagId": asset.tagId, "name": asset.studentName,
                                              "department": asset.department, "phoneNumber": asset.phoneNumber, "mailId": asset.mailId,
                                              "day_1": monthlyattendance[monthlyattendance.count() - 1].day_1,
                                              "day_2": monthlyattendance[monthlyattendance.count() - 1].day_2,
                                              "day_3": monthlyattendance[monthlyattendance.count() - 1].day_3,
                                              "day_4": monthlyattendance[monthlyattendance.count() - 1].day_4,
                                              "day_5": monthlyattendance[monthlyattendance.count() - 1].day_5,
                                              "day_6": monthlyattendance[monthlyattendance.count() - 1].day_6,
                                              "day_7": monthlyattendance[monthlyattendance.count() - 1].day_7,
                                              "day_8": monthlyattendance[monthlyattendance.count() - 1].day_8,
                                              "day_9": monthlyattendance[monthlyattendance.count() - 1].day_9,
                                              "day_10": monthlyattendance[monthlyattendance.count() - 1].day_10,
                                              "day_11": monthlyattendance[monthlyattendance.count() - 1].day_11,
                                              "day_12": monthlyattendance[monthlyattendance.count() - 1].day_12,
                                              "day_13": monthlyattendance[monthlyattendance.count() - 1].day_13,
                                              "day_14": monthlyattendance[monthlyattendance.count() - 1].day_14,
                                              "day_15": monthlyattendance[monthlyattendance.count() - 1].day_15,
                                              "day_16": monthlyattendance[monthlyattendance.count() - 1].day_16,
                                              "day_17": monthlyattendance[monthlyattendance.count() - 1].day_17,
                                              "day_18": monthlyattendance[monthlyattendance.count() - 1].day_18,
                                              "day_19": monthlyattendance[monthlyattendance.count() - 1].day_19,
                                              "day_20": monthlyattendance[monthlyattendance.count() - 1].day_20,
                                              "day_21": monthlyattendance[monthlyattendance.count() - 1].day_21,
                                              "day_22": monthlyattendance[monthlyattendance.count() - 1].day_22,
                                              "day_23": monthlyattendance[monthlyattendance.count() - 1].day_23,
                                              "day_24": monthlyattendance[monthlyattendance.count() - 1].day_24,
                                              "day_25": monthlyattendance[monthlyattendance.count() - 1].day_25,
                                              "day_26": monthlyattendance[monthlyattendance.count() - 1].day_26,
                                              "day_27": monthlyattendance[monthlyattendance.count() - 1].day_27,
                                              "day_28": monthlyattendance[monthlyattendance.count() - 1].day_28,
                                              "day_29": monthlyattendance[monthlyattendance.count() - 1].day_29,
                                              "day_30": monthlyattendance[monthlyattendance.count() - 1].day_30,
                                              "day_31": monthlyattendance[monthlyattendance.count() - 1].day_31,

                                              })
                else:
                    attendancePayload.append({"tagId": asset.tagId, "name": asset.studentName,
                                              "department": asset.department, "phoneNumber": asset.phoneNumber, "mailId": asset.mailId})
            return Response({"attendance": attendancePayload}, status=status.HTTP_200_OK)

        except Exception as err:
            print(err)
            return Response(status=status.HTTP_400_BAD_REQUEST)
