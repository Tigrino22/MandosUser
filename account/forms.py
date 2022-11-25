from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from .models import TrainUser


class RegisterForm(UserCreationForm):

    firstname = forms.CharField(
        max_length = 100,
        required = False,
        widget = forms.TextInput(attrs = {
            'class' : 'form-control',
            'placeholder' : 'Prénom'
        })
    )
    lastname = forms.CharField(
        max_length = 100,
        required = False,
        widget = forms.TextInput(attrs = {
            'placeholder' : 'Nom',
            'class' : 'form-control'
        })
    )
    email = forms.EmailField(
        required = True,
        widget = forms.TextInput(attrs = {
            'class' : 'form-control',
            'placeholder' : 'E-mail'
        })
    )
    password1 = forms.CharField(
        max_length = 50,
        required = True,
        widget= forms.TextInput(attrs= {
            'type' : 'password',
            'class' : 'form-control',
            'placeholder' : 'Mot de passe',
            'data-toggle' : 'password',
            'id' : 'password'
        })
    )
    password2 = forms.CharField(
        max_length = 50,
        required = True,
        widget= forms.TextInput(attrs= {
            'type' : 'password',
            'class' : 'form-control',
            'placeholder' : 'Confirmez votre mot de passe',
            'data-toggle' : 'password',
            'id' : 'password'
        })
    )

    class Meta:

        model = TrainUser
        fields = ['firstname', 'lastname', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):


    # Username pour le formaulaire, mais il s'agit bien de
    # l'e-mail qui est demandé sur la vue
    username = forms.EmailField(
        required = True,
        widget = forms.TextInput(attrs = {
            'class' : 'form-control',
            'placeholder' : 'E-mail'
        })
    )

    password = forms.CharField(
        max_length = 50,
        required = True,
        widget= forms.TextInput(attrs= {
            'type' : 'password',
            'class' : 'form-control',
            'placeholder' : 'Mot de passe',
            'data-toggle' : 'password',
            'id' : 'password'
        })
    )
    
    remember_me = forms.BooleanField(required=False)

    class Meta:

        model = TrainUser


