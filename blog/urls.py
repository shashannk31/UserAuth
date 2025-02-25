from django.urls import path
from .views import create_blog_post, doctor_blogs, patient_blog_list

urlpatterns = [
    path('new/', create_blog_post, name='create_blog'),
    path('my_blogs/', doctor_blogs, name='doctor_blogs'),
    path('', patient_blog_list, name='patient_blogs'),  
]
