from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignupForm(UserCreationForm):
    profile_picture = forms.ImageField(required=False)
    address_line1 = forms.CharField(max_length=255, required=True)
    city = forms.CharField(max_length=100, required=True)
    state = forms.CharField(max_length=100, required=True)
    pincode = forms.CharField(max_length=10, required=True)
    user_type = forms.ChoiceField(choices=(('patient', 'Patient'), ('doctor', 'Doctor')), required=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2',
                  'profile_picture', 'address_line1', 'city', 'state', 'pincode', 'user_type']
