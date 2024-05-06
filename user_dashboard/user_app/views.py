# user_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from django.contrib import messages
from .forms import SignUpForm

from django.contrib import messages
import logging

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        try:
            if form.is_valid():
                user = form.save()
                login(request, user)
                  # Add a success message
                messages.success(request, 'User successfully created')

            # Redirect to the login page
                return redirect('user_login')
            else:
                # Display form errors to the user
                for field, errors in form.errors.items():
                    messages.error(request, f"{field}: {', '.join(errors)}")
        except Exception as e:
            logging.error(f'Error during signup: {e}')
            messages.error(request, 'An unexpected error occurred. Please try again later.')
    else:
        form = SignUpForm()

    return render(request, 'index.html', {'form': form})


def patient_dashboard(request):
    return render(request, 'patient_dashboard.html', {'user': request.user})

def doctor_dashboard(request):
    return render(request, 'doctor_dashboard.html', {'user': request.user})



def user_login(request):
    if request.method == 'POST':
         
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
           
            if user.user_type == 'patient':
                return redirect('patient_dashboard')
            elif user.user_type == 'doctor':
                return redirect('doctor_dashboard')
            elif  user is not None:
                # User exists, but password is incorrect
                messages.error(request, 'Invalid password')
            else:
                # User with the given username does not exist
                messages.error(request, 'Invalid login credentials')
        else:
            messages.error(request, 'USER NOT FOUND')


    return render(request, 'login.html', {'login_error': messages.get_messages(request)})

