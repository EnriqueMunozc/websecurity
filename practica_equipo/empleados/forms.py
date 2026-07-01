from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):

    class Meta:

        model = Empleado

        fields = "__all__"

        widgets = {

            "nombre": forms.TextInput(attrs={"class": "form-control"}),

            "apellido": forms.TextInput(attrs={"class": "form-control"}),

            "correo": forms.EmailInput(attrs={"class": "form-control"}),

            "departamento": forms.TextInput(attrs={"class": "form-control"}),

        }