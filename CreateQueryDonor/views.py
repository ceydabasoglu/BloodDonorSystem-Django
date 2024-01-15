# CreateQueryDonor/views.py
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DonorSerializer
from .models import Donor
from .forms import DonorForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login


def branch_login(request):
    if request.method == 'POST':
        branch_name = request.POST['branch_name']
        password = request.POST['password']
        branch = authenticate(request, username=branch_name, password=password)

        if branch is not None:
            login(request, branch)
            request.session['current_branch'] = branch.username  # Kullanıcı adını oturuma ekle
            return redirect('create_query_donors')
        else:
            messages.error(request, 'Invalid branch name or password.')

    return render(request, 'branch_login.html')

@login_required
def create_query_donors(request):
    # Şube adını oturumdan al
    current_branch = request.session.get('current_branch', None)

    if current_branch is None:
        # Eğer şube adı oturumda yoksa, giriş yapma sayfasına yönlendir
        return redirect('branch_login')

    form = DonorForm()
    if request.method == 'POST':
        form = DonorForm(request.POST, request.FILES)
        if form.is_valid():
            donor = form.save(commit=False)
            donor.branch_name = current_branch  # Şube adını kaydet
            donor.save()

            messages.success(request, 'Donor successfully created.')
            return redirect('create_query_donors')
        else:
            messages.warning(request, 'Form is not valid. Please check the errors below.')

    # Sadece o şubeye ait donorleri getir
    donors = Donor.objects.filter(branch_name=current_branch)
    return render(request, 'create_query_donors.html', {'donors': donors, 'form': form, 'current_branch': current_branch})

def edit_donor(request, donor_id):
    donor = get_object_or_404(Donor, id=donor_id)

    if request.method == 'POST':
        form = DonorForm(request.POST, request.FILES, instance=donor)
        if form.is_valid():
            form.save()
            return redirect('create_query_donors')
    else:
        form = DonorForm(instance=donor)

    donors = Donor.objects.all()
    return render(request, 'create_query_donors.html', {'form': form, 'donors': donors})

def delete_donor(request, donor_id):
    donor = get_object_or_404(Donor, id=donor_id)
    donor.delete()
    return redirect('create_query_donors')

@api_view(['GET', 'POST'])
def donor_list(request):
    if request.method == 'GET':
        donors = Donor.objects.all()
        serializer = DonorSerializer(donors, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DonorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
