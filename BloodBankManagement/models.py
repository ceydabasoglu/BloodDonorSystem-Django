#BloodBankManagement/models.py
from django.db import models
from CreateQueryDonor.models import Donor

class BloodBank(models.Model):
    blood_type = models.CharField(max_length=10)
    quantity = models.IntegerField()
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE, null=True, blank=True)
    donation_date = models.DateField(auto_now_add=True)
    


    def __str__(self):
        return f"{self.blood_type} - {self.quantity} units - Donor: {self.donor.fullname if self.donor else 'None'}"
