# printer_app/urls.py
from django.urls import path
from .views import print_qr_code

urlpatterns = [
    path('print/', print_qr_code, name='print_qr_code'),
]