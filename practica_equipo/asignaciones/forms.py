from django import forms
from .models import Asignacion
from inventario.models import Equipo

class AsignacionForm(forms.ModelForm):

    class Meta:
        model = Asignacion
        fields = "__all__"

        widgets = {
            "empleado": forms.Select(attrs={"class": "form-select"}),
            "equipo": forms.Select(attrs={"class": "form-select"}),
            "fecha_asignacion": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),
            "observaciones": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["equipo"].queryset = Equipo.objects.filter(
            estado="Disponible"
        )