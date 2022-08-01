from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

app_name = 'receptions'


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path(
        'patient/',
        PatientsList.as_view(),
        name='patients'
    ),
    path(
        'patient/<int:pk>/',
        login_required(PatientDetail.as_view()),
        name='patient'
    ),
    path(
        'patient/create/',
        login_required(PatientCreate.as_view()),
        name='create_patient'
    ),
    path(
        'patient/<int:pk>/update/',
        login_required(PatientUpdate.as_view()),
        name='update_patient'
    ),
    path(
        'reception/',
        login_required(ReceptionsList.as_view()),
        name='receptions'
    ),
    path(
        'reception/<int:pk>/',
        login_required(ReceptionDetail.as_view()),
        name='reception'
    ),
    path(
        'reception/create/',
        login_required(ReceptionCreate.as_view()),
        name='create_reception'
    ),
    path(
        'reception/<int:pk>/update/',
        login_required(ReceptionUpdate.as_view()),
        name='update_reception'
    ),
    path(
        'reception/<int:pk>/delete/',
        login_required(ReceptionDelete.as_view()),
        name='delete_reception'
    ),
    path(
        'diagnosis/',
        DiagnosisList.as_view(),
        name='diagnoses'
    ),
    path(
        'diagnosis/create/',
        login_required(DiagnosisCreate.as_view()),
        name='create_diagnosis'
    ),
    path(
        'diagnosis/<int:pk>/update/',
        login_required(DiagnosisUpdate.as_view()),
        name='update_diagnosis'
    ),
    path(
        'diagnosis/<int:pk>/delete/',
        login_required(DiagnosisDelete.as_view()),
        name='delete_diagnosis'
    ),
    path(
        'procedure/',
        ProcedureList.as_view(),
        name='procedures'
    ),
    path(
        'procedure/create/',
        login_required(ProcedureCreate.as_view()),
        name='create_procedure'
    ),
    path(
        'procedure/<int:pk>/update/',
        login_required(ProcedureUpdate.as_view()),
        name='update_procedure'
    ),
    path(
        'procedure/<int:pk>/delete/',
        login_required(ProcedureDelete.as_view()),
        name='delete_procedure'
    )
]