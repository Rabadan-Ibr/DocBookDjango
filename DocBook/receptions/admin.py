from django.contrib import admin

from .models import Diagnosis, Patient, Procedure, Reception

admin.site.register([Diagnosis,Procedure, Patient, Reception])
