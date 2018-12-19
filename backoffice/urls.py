from django.urls import path

from backoffice.views import *

app_name = 'bo'
urlpatterns = [
    path('', Index.as_view(), name='index'),

    path('animal/list/', AnimalList.as_view(), name='animal_list'),
    path('animal/add/', AnimalAdd.as_view(), name='animal_add'),
    path('animal/edit/<int:pk>/', AnimalEdit.as_view(), name='animal_edit'),
    path('animal/delete/<int:pk>/', AnimalDelete.as_view(), name='animal_delete'),
    path('animal/detail/<int:pk>/', AnimalDetail.as_view(), name='animal_detail'),

    path('diagnostico/list/', DiagnosticoList.as_view(), name='diagnostico_list'),
    path('diagnostico/add/', DiagnosticoAdd.as_view(), name='diagnostico_add'),
    path('diagnostico/edit/<int:pk>/', DiagnosticoEdit.as_view(), name='diagnostico_edit'),
    path('diagnostico/delete/<int:pk>/', DiagnosticoDelete.as_view(), name='diagnostico_delete'),
    path('diagnostico/detail/<int:pk>/', DiagnosticoDetail.as_view(), name='diagnostico_detail'),

    path('historial/list/', HistorialList.as_view(), name='historial_list'),
    path('historial/add/', HistorialAdd.as_view(), name='historial_add'),
    path('historial/edit/<int:pk>/', HistorialEdit.as_view(), name='historial_edit'),
    path('historial/delete/<int:pk>/', HistorialDelete.as_view(), name='historial_delete'),
    path('historial/detail/<int:pk>/', HistorialDetail.as_view(), name='historial_detail'),

    path('paciente/list/', PacienteList.as_view(), name='paciente_list'),
    path('paciente/add/', PacienteAdd.as_view(), name='paciente_add'),
    path('paciente/edit/<int:pk>/', PacienteEdit.as_view(), name='paciente_edit'),
    path('paciente/delete/<int:pk>/', PacienteDelete.as_view(), name='paciente_delete'),
    path('paciente/detail/<int:pk>/', PacienteDetail.as_view(), name='paciente_detail'),

    path('raza/list/', RazaList.as_view(), name='raza_list'),
    path('raza/add/', RazaAdd.as_view(), name='raza_add'),
    path('raza/edit/<int:pk>/', RazaEdit.as_view(), name='raza_edit'),
    path('raza/delete/<int:pk>/', RazaDelete.as_view(), name='raza_delete'),
    path('raza/detail/<int:pk>/', RazaDetail.as_view(), name='raza_detail'),

    path('api/v1/animal/', ApiAnimalList.as_view()),
    path('api/v1/diagnostico/', ApiDiagnosticoList.as_view()),
    path('api/v1/historial/', ApiHistorialList.as_view()),
    path('api/v1/paciente/', ApiPacienteList.as_view()),
    path('api/v1/raza/', ApiRazaList.as_view()),

    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
