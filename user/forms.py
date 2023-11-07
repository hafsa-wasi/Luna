# from django.core import validators
from django.forms import ModelForm
from django.forms import TextInput
from django import forms
from .models import profile


class profileForm(forms.ModelForm):
   photo = forms.ImageField(required=False)
   class Meta:
      model = profile
      fields = {'photo','email'}
      
      labels = {
        "photo" : "Image",
        # "user"  : "Username",
        "email" : "Email Id"
      }
      widgets = {
            'email': TextInput(attrs={
                'required' : "",
                'class': "from-control",
                'id':'home',
                'style': 'position:relative; padding: 10px;padding-inline-start: 20px;background-color: var(--bg-prussian-blue);border-radius: var(--radius-6);border: 1px solid var(--bg-carolina-blue);display: flex;justify-items: flex-end;transition: var(--transition-1);',
                'placeholder': 'Enter your Email Address.'
                }),
            
      }



# #Create the form class.
# class signinForm(forms.ModelForm):
#    class Meta:
#       model = user
      
#       fields = {'Email','password'}
#       widgets = {
#         'password': forms.PasswordInput(),
#         }
#       labels = {
#          "Email" : "Email Id",
#          "password" : "Password",
#          }
    