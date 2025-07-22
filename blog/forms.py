from django import forms
from blog.models import * 
from django.contrib.auth.models import User


class Myforms(forms.Form):

    first_name=forms.CharField(required=True)
    last_name=forms.CharField(required=True)
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':"john@gmail.com",'class':'border-3 rounded-lg'}))
    description_text=forms.CharField(widget=forms.Textarea)

    def clean_email(self):
        email=self.cleaned_data['email']
        if News.objects.filter(email=email).exists():
            raise forms.ValidationError("email exist!! ")
        return email
        

    def save(self):
        return News.objects.create(first_name=self.cleaned_data['first_name'],
                                   last_name=self.cleaned_data['last_name'],
                                   email=self.cleaned_data['email'],
                                   description=self.cleaned_data['description_text'],
                                   )

class NewsForm(forms.ModelForm):
    date_of_birth=forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'date'}))
    class Meta:
        model=News
        fields=['first_name','last_name','date_of_birth','email','description']
    
    def clean_first_name(self):
        first_name=self.cleaned_data['first_name']
        if "admin" in first_name.lower():
            raise forms.ValidationError("first name should not contain 'admin'")
        return first_name
class BookForm(forms.ModelForm):
    publish_date=forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type':'date'}))
    class Meta:
        model=Book
        fields=['title','author','publish_date']


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
