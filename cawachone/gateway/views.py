from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Gateway
from .serializers import GatewaySerializers


class GatewayRegistration(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request):
        try:
            gate = Gateway()
            gate.gatewayId = request.data.get("gatewayId")
            gate.gatewayName = request.data.get("gatewayName")
            gate.timestamp = "-:-:-"
            gate.save()

            return Response(status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GatewayDetails(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        try:
            gateways = GatewaySerializers(Gateway.objects.all(), many=True)
            return Response({"gateways": gateways.data}, status=status.HTTP_200_OK)
        except Exception as err:
            print(err)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GatewayDeletion(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @staticmethod                                                                                                           
    def post(request):
        try:
            asset = Gateway.objects.get(gatewayId=request.data.get("gatewayId").lower())
            asset.delete()
            return Response(status=status.HTTP_200_OK)
        except Exception as err:
            return Response(status=status.HTTP_400_BAD_REQUEST)
