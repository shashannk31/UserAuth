from django.urls import path
from .views import signup_view, login_view, logout_view, patient_dashboard, doctor_dashboard
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('patient/dashboard/', patient_dashboard, name='patient_dashboard'),
    path('doctor/dashboard/', doctor_dashboard, name='doctor_dashboard'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
