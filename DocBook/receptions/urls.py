from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import Index, PatientsList, ReceptionsList, PatientDetail, ReceptionDetail, PatientCreate, ReceptionCreate

app_name = 'receptions'


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('patient/', PatientsList.as_view(), name='patients'),
    path('patient/create/', PatientCreate.as_view(), name='create_patient'),
    path('reception/', ReceptionsList.as_view(), name='receptions'),
    path(
        'reception/create/',
        login_required(ReceptionCreate.as_view(), login_url='auth:login'),
        name='create_reception'
    ),
    path('patient/<int:pk>/', PatientDetail.as_view(), name='patient'),
    path('reception/<int:pk>/', ReceptionDetail.as_view(), name='reception'),
]