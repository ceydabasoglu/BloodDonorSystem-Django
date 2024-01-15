# BloodBankManagement/urls.py
from django.urls import path
from .views import add_blood_to_bank, get_donor_info, delete_blood_bank

urlpatterns = [
    path('add_blood_to_bank/', add_blood_to_bank, name='add_blood_to_bank'),
    path('get_donor_info/<int:donor_id>/', get_donor_info, name='get_donor_info'),
    path('delete_blood_bank/<int:blood_bank_id>/', delete_blood_bank, name='delete_blood_bank'),

]
