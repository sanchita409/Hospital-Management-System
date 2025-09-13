from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CustomLoginForm



def index(request):
    return render(request,'index.html')


def login_view(request):
    login_type = request.GET.get('type', '')
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            # Allow superuser to login from any panel
            if user.is_superuser:
                login(request, user)
                return redirect('admin_dashboard')
            # Match user role with selected login type
            if login_type == user.role.lower():
                login(request, user)
                if user.role.lower() == 'doctor':
                    return redirect('doctor_dashboard')
                elif user.role.lower() == 'patient':
                    return redirect('patient_dashboard')
                elif user.role.lower() == 'admin':
                    return redirect('admin_dashboard')
            else:
                messages.error(request, "Unauthorized role access.")
        else:
            messages.error(request, "Please enter a correct username and password.")
    else:
        form = CustomLoginForm()

    return render(request, 'accounts/login.html', {'form': form, 'login_type': login_type})

def admin_dashboard(request):
    return render(request, 'accounts/admin_dashboard.html')

def doctor_dashboard(request):
    return render(request, 'accounts/doctor_dashboard.html')

def patient_dashboard(request):
    return render(request, 'accounts/patient_dashboard.html')

