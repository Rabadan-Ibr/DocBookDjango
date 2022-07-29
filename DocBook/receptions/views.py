from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from . models import Patient, Reception


class Index(TemplateView):
    template_name = 'receptions/index.html'


class PatientView(ListView):
    model = Patient


class ReceptionsView(ListView):
    model = Reception
