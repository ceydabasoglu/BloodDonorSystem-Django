"""
URL configuration for BloodDonorSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# BloodDonorSystem/urls.py
from django.contrib import admin
from django.urls import path, include
from CreateQueryDonor.views import create_query_donors
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bloodbank/', include('BloodBankManagement.urls')),
    path('create_query_donor/', include('CreateQueryDonor.urls')),
    path('bloodrequest/', include('BloodRequestManagement.urls')),
    path('login/', LoginView.as_view(), name='login'),  
    path('', create_query_donors, name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('bloodbank/', include('BloodBankManagement.urls')),
       
]
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/create_query_donor/'

