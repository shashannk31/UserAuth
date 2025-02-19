from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.user_type == 'patient':
                return redirect('patient_dashboard')
            else:
                return redirect('doctor_dashboard')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.user_type == 'patient':
                return redirect('patient_dashboard')
            else:
                return redirect('doctor_dashboard')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password'})
    return render(request, 'accounts/login.html')



def logout_view(request):
    logout(request)
    return redirect('login')



@login_required
def patient_dashboard(request):
    return render(request, 'accounts/patient_dashboard.html', {'user': request.user})



@login_required
def doctor_dashboard(request):
    return render(request, 'accounts/doctor_dashboard.html', {'user': request.user})
