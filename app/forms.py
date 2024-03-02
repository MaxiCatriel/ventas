from django import forms
from .models import Evento
from django.contrib.auth.forms  import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class  FormularioEventos(forms.ModelForm):
    class Meta:
        model = Evento
        fields='__all__'
        
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'password1', 'password2']