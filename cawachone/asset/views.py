from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Asset, AssetHealth
from .serializers import AssetSerializers, AssetHealthSerializers
from attendance.models import DailyReport, AttendanceSheet


class AssetRegistration(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request):
        try:
            var = Asset()
            var.studentName = request.data.get("studentName")
            var.tagId = request.data.get("tagId")
            var.registrationNo = request.data.get("registrationNo")
            var.department = request.data.get("department")
            var.phoneNumber = request.data.get("phoneNumber")
            var.mailId = request.data.get("mailId")
            var.gender = request.data.get("gender")
            var.save()

            atn = DailyReport()
            atn.tagId = var
            atn.save()

            mns = AttendanceSheet()
            mns.tagId = var
            mns.save()

            return Response(status=status.HTTP_201_CREATED)
        except Exception as err:
            print(type(err))
            print(err)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class AssetDetails(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        try:
            assets = Asset.objects.all()
            assets = AssetSerializers(assets, many=True)
            if assets!=None:
                return Response({"assets": assets.data}, status=status.HTTP_200_OK)
            else:
                return Response({"assets": []}, status=status.HTTP_404_NOT_FOUND)
        except Exception as err:
            print(err)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class AssetDeletion(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request):
        try:
            asset = Asset.objects.get(tagId=request.data.get("tagId").lower())
            asset.delete()
            return Response(status=status.HTTP_200_OK)
        except Exception as err:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class AssetHealthApi(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        try:

            assethealthPayload = []
            for asset in Asset.objects.all():
                print(asset.studentName)
                assethealth = AssetHealth.objects.filter(asset=asset)
                print(assethealth)
                if assethealth.exists():
                    assethealthPayload.append(
                        {"tagId": asset.tagId, "name": asset.studentName,"department":asset.department, "phoneNumber":asset.phoneNumber, "mailId":asset.mailId,
                         "lastseen": assethealth[assethealth.count() - 1].lastseen,
                         "battery": assethealth[assethealth.count() - 1].battery})

            return Response({"assets": assethealthPayload}, status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class StudentDetails(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request):
        try:
            studentdetail = Asset.objects.get(tagId=request.data.get('tagId'))
            serializer = AssetSerializers(studentdetail)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UpdateStudent(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def put(request):
        try:
            asset = Asset.objects.get(tagId=request.data.get("tagId"))
            # asset = Asset.objects.get(registrationNo= request.get("registrationNo"))
            asset.studentName = request.data.get("studentName")
            asset.tagId = request.data.get("tagId")
            asset.registrationNo = request.data.get("registrationNo")
            asset.department = request.data.get("department")
            asset.phoneNumber = request.data.get("phoneNumber")
            asset.mailId = request.data.get("mailId")
            asset.gender = request.data.get("gender")
            asset.save()
            serializer = AssetSerializers(asset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response(status=status.HTTP_400_BAD_REQUEST)
