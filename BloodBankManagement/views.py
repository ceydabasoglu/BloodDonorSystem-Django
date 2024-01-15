# BloodBankManagement/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import BloodBank
from CreateQueryDonor.models import Donor, BloodBankBranch
from .forms import BloodBankForm
from django.http import JsonResponse
from django.contrib import messages

@login_required
def add_blood_to_bank(request):
    branch_name = "Kızılay İzmir-Konak" 
    donors = Donor.objects.all()
    branch = get_object_or_404(BloodBankBranch, branch_name=branch_name)
    branch_welcome_message = f"Add Blood {branch.branch_name} branch"

    if request.method == 'POST':
        form = BloodBankForm(request.POST)
        if form.is_valid():
            # Formu kaydetmeden önce blood_type'ı doğrudan al
            blood_type = Donor.objects.get(id=request.POST['donor']).blood_type
            form.instance.blood_type = blood_type
            form.save()
            messages.success(request, 'Blood successfully added to the bank.')
            return redirect('add_blood_to_bank')  
    
    else:
        form = BloodBankForm()

    
    blood_banks = BloodBank.objects.all()
    return render(request, 'add_blood_to_bank.html', {'form': form, 'donors': donors, 'blood_banks': blood_banks, 'branch_welcome_message': branch_welcome_message})


def get_donor_info(request, donor_id):
    donor = get_object_or_404(Donor, id=donor_id)
    donor_info = {
        'blood_type': donor.blood_type,
        'donor_name': donor.fullname,
    }
    return JsonResponse(donor_info)

@login_required
def delete_blood_bank(request, blood_bank_id):
    blood_bank = get_object_or_404(BloodBank, id=blood_bank_id)
    blood_bank.delete()
    messages.success(request, 'Blood bank entry successfully deleted.')
    return redirect('add_blood_to_bank')
