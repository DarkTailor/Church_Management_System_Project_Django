from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse

from .models import Donations
from users.models import UserProfile
from .forms import DonationsForm
import csv
from django.http import HttpResponse
from django.views import View
from Donations.models import Donations  # Replace with your actual model


class DownloadCSVViewDonations(View):
    def get(self, request, *args, **kwargs):
        # Fetch data from your model
        queryset = Donations.objects.all()  # Replace with your actual queryset

        # Create CSV response
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="exported_data.csv"'

        # Write CSV data to the response
        writer = csv.writer(response)
        writer.writerow(['type', 'amount', 'description'])  # Replace with your actual field names
        for item in queryset:
            writer.writerow([item.type, item.amount, item.description])  # Use the actual attribute names

        return response


@login_required
def list_donations(request):
    template = "Donations/list.html"
    donations = Donations.objects.all()
    profile = UserProfile.objects.get_or_create(user=request.user)
    context = {"donations": donations, "donations_active_list": "active", "profile": profile}
    return render(request, template, context)

@login_required
def add_donation(request):
    # TODO: Make this functionality available only to admins
    template = "Donations/add.html"
    form = DonationsForm()
    profile = UserProfile.objects.get_or_create(user=request.user)
    context = {"form": form, "donations_active_add": "active", "profile": profile}
    return render(request, template, context)

@login_required
def create_donation(request):
    # TODO: Make this functionality available only to admins
    if request.method == "POST":
        form = DonationsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Donation added successfully")
            return redirect('list_donations')
        else:
            messages.error(request, "Donation creation failed. Please check the form.")
            return redirect('add_donation')








def api_get_donations(request):
    Donations = Donations.objects.all()
    data = {"Donations": Donations}
    return JsonResponse(data, content_type="Application/json", safe=False)


def api_create_donation(request):
    if request.method == "POST":
        form = DonationsForm(request.POST, request.FILES or None)
        if form.is_valid():
            Donations = form.save(commit=False)
            Donations.save()
            data = {"STATUS": "OK", "SHEPHERD_ID": shepherd.pk}
            return JsonResponse(data, content_type="Application/json", safe=False)
        else:
            data = {"STATUS": "INVALID"}
            return JsonResponse(data, content_type="Application/json", safe=False)


def api_edit_donation(request, pk):
    if request.method == "POST":
        Donations = get_object_or_404(Donations, pk=pk)
        form = DonationsForm(request.POST or None, instance=Donations)
        if form.is_valid():
            form.save()
            data = {"STATUS": "OK", "CODE": 0}
        else:
            data = {"STATUS": "INVALID", "CODE": -1}
        return JsonResponse(data, content_type="Application/json", safe=False)


def api_delete_donation(request, pk):
    if request.method == "POST":
        Donations = get_object_or_404(Donations, pk=pk)
        form = DonationsForm(request.POST or None, instance=Donations)
        if form.is_valid():
            form.delete()
            data = {"STATUS": "OK", "CODE": 0}
        else:
            data = {"STATUS": "INVALID", "CODE": -1}
        return JsonResponse(data, content_type="Application/json", safe=False)

