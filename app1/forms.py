from django import forms
from app1.models import Cliente

class ClienteModelForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['nome', 'sobrenome', 'email']