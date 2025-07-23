from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )

class CreatingUserFrom(forms.Form):
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    email=forms.EmailField()
    password=forms.CharField(max_length=100)
    confirm_password=forms.CharField(max_length=100)
 
    
    def clean_email(self):
        email=self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("email exist!! ")
        return email
    
    def clean(self):
        password=self.cleaned_data['password']
        confirm_password=self.cleaned_data['confirm_password']
        
        if confirm_password!=password:
            raise forms.ValidationError("password not match ")

    
    def save(self):
        return User.objects.create_user(first_name=self.cleaned_data['first_name'],
                                   last_name=self.cleaned_data['last_name'],
                                   email=self.cleaned_data['email'],
                                   username=self.cleaned_data['email'],
                                   password=self.cleaned_data['password'],
                                   )