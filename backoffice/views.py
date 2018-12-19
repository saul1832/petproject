from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *

from backoffice.forms import *
from backoffice.models import *


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = reverse_lazy("bo:index")

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class LogoutView(LoginRequiredMixin, RedirectView):
    pattern_name = 'bo:index'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class Index(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['msg'] = 'Inicio'
        return context


class AnimalList(LoginRequiredMixin, ListView):
    template_name = 'animal/list.html'
    model = Animal


class AnimalAdd(LoginRequiredMixin, CreateView):
    template_name = 'base/add.html'
    model = Animal
    form_class = AnimalForm
    success_url = reverse_lazy('bo:animal_list')


class AnimalEdit(LoginRequiredMixin, UpdateView):
    template_name = 'base/edit.html'
    model = Animal
    form_class = AnimalForm
    success_url = reverse_lazy('bo:animal_list')


class AnimalDelete(LoginRequiredMixin, DeleteView):
    template_name = 'base/delete.html'
    model = Animal
    success_url = reverse_lazy('bo:animal_list')


class AnimalDetail(LoginRequiredMixin, DetailView):
    template_name = 'base/detail.html'
    model = Animal


class DiagnosticoList(LoginRequiredMixin, ListView):
    template_name = 'diagnostico/list.html'
    model = Diagnostico


class DiagnosticoAdd(LoginRequiredMixin, CreateView):
    template_name = 'base/add.html'
    model = Diagnostico
    form_class = DiagnosticoForm
    success_url = reverse_lazy('bo:diagnostico_list')


class DiagnosticoEdit(LoginRequiredMixin, UpdateView):
    template_name = 'base/edit.html'
    model = Diagnostico
    form_class = DiagnosticoForm
    success_url = reverse_lazy('bo:diagnostico_list')


class DiagnosticoDelete(LoginRequiredMixin, DeleteView):
    template_name = 'base/delete.html'
    model = Diagnostico
    success_url = reverse_lazy('bo:diagnostico_list')


class DiagnosticoDetail(LoginRequiredMixin, DetailView):
    template_name = 'base/detail.html'
    model = Diagnostico


class HistorialList(LoginRequiredMixin, ListView):
    template_name = 'historial/list.html'
    model = Historial


class HistorialAdd(LoginRequiredMixin, CreateView):
    template_name = 'base/add.html'
    model = Historial
    form_class = HistorialForm
    success_url = reverse_lazy('bo:historial_list')


class HistorialEdit(LoginRequiredMixin, UpdateView):
    template_name = 'base/edit.html'
    model = Historial
    form_class = HistorialForm
    success_url = reverse_lazy('bo:historial_list')


class HistorialDelete(LoginRequiredMixin, DeleteView):
    template_name = 'base/delete.html'
    model = Historial
    success_url = reverse_lazy('bo:historial_list')


class HistorialDetail(LoginRequiredMixin, DetailView):
    template_name = 'base/detail.html'
    model = Historial


class PacienteList(LoginRequiredMixin, ListView):
    template_name = 'paciente/list.html'
    model = Paciente


class PacienteAdd(LoginRequiredMixin, CreateView):
    template_name = 'base/add.html'
    model = Paciente
    form_class = PacienteForm
    success_url = reverse_lazy('bo:paciente_list')


class PacienteEdit(LoginRequiredMixin, UpdateView):
    template_name = 'base/edit.html'
    model = Paciente
    form_class = PacienteForm
    success_url = reverse_lazy('bo:paciente_list')


class PacienteDelete(LoginRequiredMixin, DeleteView):
    template_name = 'base/delete.html'
    model = Paciente
    success_url = reverse_lazy('bo:paciente_list')


class PacienteDetail(LoginRequiredMixin, DetailView):
    template_name = 'base/detail.html'
    model = Paciente


class RazaList(LoginRequiredMixin, ListView):
    template_name = 'raza/list.html'
    model = Raza


class RazaAdd(LoginRequiredMixin, CreateView):
    template_name = 'base/add.html'
    model = Raza
    form_class = RazaForm
    success_url = reverse_lazy('bo:raza_list')


class RazaEdit(LoginRequiredMixin, UpdateView):
    template_name = 'base/edit.html'
    model = Raza
    form_class = RazaForm
    success_url = reverse_lazy('bo:raza_list')


class RazaDelete(LoginRequiredMixin, DeleteView):
    template_name = 'base/delete.html'
    model = Raza
    success_url = reverse_lazy('bo:raza_list')


class RazaDetail(LoginRequiredMixin, DetailView):
    template_name = 'base/detail.html'
    model = Raza


