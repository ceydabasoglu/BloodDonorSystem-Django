# CreateQueryDonor/forms.py
from django import forms
from .models import Donor, BloodBankBranch

class DonorForm(forms.ModelForm):
    branch = forms.ModelChoiceField(queryset=BloodBankBranch.objects.all(), required=False, label='Branch')
    class Meta:
        model = Donor
        fields = ['fullname', 'blood_type', 'town', 'city', 'phone_number', 'email', 'photo','units']

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if not phone_number.isdigit():
            raise forms.ValidationError("Phone number should only contain digits.")
        return phone_number
