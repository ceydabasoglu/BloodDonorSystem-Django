# CreateQueryDonor/serializers.py
from rest_framework import serializers
from .models import Donor

class DonorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donor
        fields = ['id', 'fullname', 'blood_type', 'town', 'city', 'phone_number', 'email', 'photo','units']
