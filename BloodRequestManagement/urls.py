# BloodRequestManagement/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import request_blood, BloodRequestListCreateView, request_blood_success

urlpatterns = [
    path('api/bloodrequests/', BloodRequestListCreateView.as_view(), name='bloodrequest-list-create'),
    path('request_blood/', request_blood, name='request_blood'),
    path('request_blood_success/', request_blood_success, name='request_blood_success'),
    
]