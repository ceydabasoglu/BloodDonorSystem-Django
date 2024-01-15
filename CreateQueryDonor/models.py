# CreateQueryDonor/models.py
from django.db import models
from django.core.validators import EmailValidator
from django.contrib.auth.models import User

class BloodBankBranch(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.branch_name

class Donor(models.Model):
    fullname = models.CharField(max_length=255)
    blood_type = models.CharField(max_length=10)
    town = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True, null=True, default=None, blank=True, validators=[EmailValidator()])
    photo = models.ImageField(upload_to='donor_photos/', blank=True, null=True)
    units = models.IntegerField(default=0, null=True, blank=True)
    branch_name = models.CharField(max_length=255, default="Genel")
    
    def __str__(self):
        return self.fullname



