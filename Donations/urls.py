from django.urls import path
from . import views
from .views import DownloadCSVViewDonations


urlpatterns = [
    path('list/', views.list_donations, name='list_donations'),
    path('add/', views.add_donation, name='add_donation'),
    path('create/', views.create_donation, name='create_donation'),
    path('download-csv/', DownloadCSVViewDonations.as_view(), name='download_csvDonations'),
    # Add other URL patterns as needed
]
