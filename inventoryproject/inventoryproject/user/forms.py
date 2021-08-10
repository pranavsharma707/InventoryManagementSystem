from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):#here we customize usercreation form 
    email=forms.EmailField()
    class Meta:
        model=User
        # fields='__all__'  # all means we add field of User admin to user 
        fields=["username","email","password1","password2"]#now the userform come with "username","email","password1","password2" which are inherit from user from admin
 