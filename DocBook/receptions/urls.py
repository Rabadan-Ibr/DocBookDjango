from django.urls import path
from .views import Index, PatientView, ReceptionsView

app_name = 'receptions'


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('patient/', PatientView.as_view(), name='patient'),
    path('reception/', ReceptionsView.as_view(), name='reception'),
]