from django.urls import path

from .views import *

urlpatterns = [
    path('gatewayregistration', GatewayRegistration.as_view()),
    path('gatewaydetails', GatewayDetails.as_view()),
    path('gatewaydeletion', GatewayDeletion.as_view())
]