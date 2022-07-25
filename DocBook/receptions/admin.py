from django.contrib import admin

from .models import Diagnosis, Procedure, Patient, Reception


admin.site.register([Diagnosis,Procedure, Patient, Reception])
