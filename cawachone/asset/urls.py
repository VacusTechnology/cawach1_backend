from django.urls import path

from .views import *

urlpatterns = [
    path('studentregistration', AssetRegistration.as_view()),
    path('studentdeletion', AssetDeletion.as_view()),
    path('studentdetails', AssetDetails.as_view()),
    path('studenthealth', AssetHealthApi.as_view()),
    path('updatestudent', UpdateStudent.as_view()),
    path('details', StudentDetails.as_view()),
    path('bulkupload', BulkUploadApi.as_view())
]
