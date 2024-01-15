from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt  
from .models import BloodRequest
from .forms import BloodRequestForm
from CreateQueryDonor.models import Donor
from rest_framework import generics
from .serializers import BloodRequestSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.views import FilterView
from django_filters import rest_framework as filters
from django.contrib import messages

@csrf_exempt  
def request_blood(request):
    if request.method == 'POST':
        form = BloodRequestForm(request.POST)
        if form.is_valid():
            blood_request = form.save()
            print("Blood Request Object:", blood_request)

            # Implement the logic to search for available blood
            available_donors = Donor.objects.filter(
                blood_type=blood_request.blood_type,
                town=blood_request.town,
                city=blood_request.city
            )

            print("Available Donors:", available_donors)

            if available_donors.exists():
                selected_donor = available_donors.first()
                print("Selected Donor:", selected_donor)

                send_mail(
                    'Blood Found',
                    f'Good news! Blood is available from {selected_donor.fullname} for {blood_request.requester_name} at {blood_request.hospital}.',
                    settings.DEFAULT_FROM_EMAIL,
                    [blood_request.contact_email],
                    fail_silently=False,
                )

                send_mail(
                    'Blood Used',
                    f'Your blood has been used to help {blood_request.requester_name} at {blood_request.hospital}.',
                    settings.DEFAULT_FROM_EMAIL,
                    [selected_donor.email],
                    fail_silently=False,
                )

                selected_donor.units -= blood_request.units
                selected_donor.save()

                messages.success(request, 'Kan talebiniz başarıyla alındı. En kısa sürede size uygun bir donör bulmaya çalışacağız.')
                return redirect('request_blood_success')
            else:
                print("No available donors found.")
        else:
            print("Form is not valid.")
            print("Form Errors:", form.errors)

    else:
        form = BloodRequestForm()

    return render(request, 'request_blood.html', {'form': form})

def request_blood_success(request):
    return render(request, 'request_blood_success.html')

class BloodRequestFilter(filters.FilterSet):
    class Meta:
        model = BloodRequest
        fields = ['blood_type', 'city', 'town']

#Django REST Framework, generic views. CRUD (Create, Read, Update, Delete) işlemleri.
class BloodRequestListCreateView(FilterView, generics.ListCreateAPIView):
    queryset = BloodRequest.objects.all()
    serializer_class = BloodRequestSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = BloodRequestFilter
    template_name = 'C:/Users/pc/OneDrive/Masaüstü/Se4458final/BloodDonorSystem/BloodRequestManagement/templates/request_blood.html'

    def perform_create(self, serializer):
        serializer.save(requester_name=self.request.user.username)
















        """
@csrf_exempt  
def request_blood(request):
    if request.method == 'POST':
        form = BloodRequestForm(request.POST)
        if form.is_valid():
            blood_request = form.save()

            # Implement the logic to search for available blood
            available_donors = Donor.objects.filter(
                blood_type=blood_request.blood_type,
                town=blood_request.town,
                city=blood_request.city
            )

            if available_donors.exists():
                selected_donor = available_donors.first()

                send_mail(
                    'Blood Found',
                    f'Good news! Blood is available from {selected_donor.fullname}',
                    settings.DEFAULT_FROM_EMAIL,
                    [blood_request.contact_email],
                    fail_silently=False,
                )

                send_mail(
                    'Blood Used',
                    f'Your blood has been used to help someone in need.',
                    settings.DEFAULT_FROM_EMAIL,
                    [selected_donor.email],
                    fail_silently=False,
                )

                selected_donor.units -= blood_request.units
                selected_donor.save()

                messages.success(request, 'Kan talebiniz başarıyla alındı. En kısa sürede size uygun bir donör bulmaya çalışacağız.')
                return redirect('request_blood_success') 

    else:
        form = BloodRequestForm()

    return render(request, 'request_blood.html', {'form': form})
"""