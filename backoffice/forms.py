from django import forms
from django.core.exceptions import ValidationError

from backoffice.models import *


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")

        if len(nombre) < 3:
            self.add_error('nombre', 'Nombre muy pequeño')

        existe = Animal.objects.filter(nombre__contains=nombre).exclude(id=self.instance.pk)
        if existe:
            self.add_error('nombre', 'Nombre ya existe')


class RazaForm(forms.ModelForm):
    class Meta:
        model = Raza
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class DiagnosticoForm(forms.ModelForm):
    class Meta:
        model = Diagnostico
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class HistorialForm(forms.ModelForm):
    class Meta:
        model = Historial
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
