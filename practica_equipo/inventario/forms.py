from django import forms
from .models import Equipo


class EquipoForm(forms.ModelForm):

    class Meta:

        model = Equipo

        fields = "__all__"

        widgets = {

            "codigo": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "tipo": forms.Select(attrs={
                "class": "form-select"
            }),

            "marca": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "modelo": forms.TextInput(attrs={
                "class": "form-control"
            }),

            "estado": forms.Select(attrs={
                "class": "form-select"
            }),

        }