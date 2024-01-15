# BloodRequestManagement/models.py
from django.db import models

class BloodRequest(models.Model):
    requester_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    hospital = models.CharField(max_length=255)
    town = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    blood_type = models.CharField(max_length=10)
    units = models.IntegerField()
    duration_of_search_days = models.IntegerField()
    reason = models.TextField()
    
    def __str__(self):
        return f"{self.requester_name} - {self.hospital} - {self.blood_type} - {self.units} units"
