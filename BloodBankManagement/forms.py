# BloodBankManagement/forms.py
from django import forms
from .models import BloodBank

class BloodBankForm(forms.ModelForm):
    class Meta:
        model = BloodBank
        fields = ['donor', 'quantity']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.donor:
            # Eğer form bir örneğe sahipse ve donör bilgisi varsa, blood_type alanını doldur
            self.fields['blood_type'].initial = self.instance.donor.blood_type
            # blood_type alanını devre dışı bırak, çünkü bu alanı kullanıcı değiştirememeli
            self.fields['blood_type'].widget.attrs['readonly'] = True
            self.fields['blood_type'].widget.attrs['disabled'] = True
