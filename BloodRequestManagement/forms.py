from django import forms
from .models import BloodRequest

class BloodRequestForm(forms.ModelForm):
    class Meta:
        model = BloodRequest
        fields = ['requester_name', 'contact_email', 'hospital', 'town', 'city', 'blood_type', 'units', 'duration_of_search_days', 'reason']

    # Blood Type ve Number of Units için seçenekleri ekledik
    BLOOD_TYPE_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('0+', '0+'),
        ('0-', '0-'),
    ]

    blood_type = forms.ChoiceField(choices=BLOOD_TYPE_CHOICES, widget=forms.Select(attrs={'class': 'blood-type-select'}), required=True)
    units = forms.IntegerField(min_value=1, required=True)

    