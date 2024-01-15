# CreateQueryDonor/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import create_query_donors, donor_list, edit_donor, delete_donor, branch_login

urlpatterns = [
    path('create_query_donors/', create_query_donors, name='create_query_donors'),
    path('api/donors/', donor_list, name='donor-list'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit_donor/<int:donor_id>/', edit_donor, name='edit_donor'),
    path('delete_donor/<int:donor_id>/', delete_donor, name='delete_donor'),
    path('branch_login/', branch_login, name='branch_login'),
    
    
]
