# myapp/urls.py
from django.urls import path
from .views import login_view, admin_dashboard, doctor_dashboard, patient_dashboard

urlpatterns = [
    path('login/', login_view, name='login'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('doctor_dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('patient_dashboard/', patient_dashboard, name='patient_dashboard'),
]
