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
