from django import forms
from .models import Proyecto, Herramienta
from django import forms
from .models import Proyecto, Tipo

class ProyectoForm(forms.ModelForm):
    tipo = forms.ModelChoiceField(
        queryset=Tipo.objects.all(),  # Obtiene los tipos de la base de datos
        widget=forms.Select(attrs={'class': 'form-control'})  # Mantiene el diseño Bootstrap
    )

    class Meta:
        model = Proyecto
        fields = '__all__'


class HerramientaForm(forms.ModelForm):
    class Meta:
        model = Herramienta
        fields = '__all__'
