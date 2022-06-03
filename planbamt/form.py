from pyexpat import model
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class signupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=get_user_model()
        fields=('username','email','first_name','last_name',)

class ConnexionForm(forms.Form):
      username = forms.CharField(label='Nom utilisateur', max_length=30)
      password = forms.CharField(label='mot de passe',widget=forms.PasswordInput)

            