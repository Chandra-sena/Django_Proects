# user_app/urls.py
from django.urls import path
from .views import signup, patient_dashboard, doctor_dashboard, user_login

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('patient/dashboard/', patient_dashboard, name='patient_dashboard'),
    path('doctor/dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('login/', user_login, name='user_login'),
]
