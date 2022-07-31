from django.views.generic import ListView, DetailView, TemplateView, CreateView
from . models import Patient, Reception


class Index(TemplateView):
    template_name = 'receptions/index.html'


class PatientsList(ListView):
    model = Patient


class ReceptionsList(ListView):
    model = Reception


class PatientDetail(DetailView):
    model = Patient

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['receptions'] = self.get_object().receptions.all()
        return context


class PatientCreate(CreateView):
    model = Patient
    fields = ['name', 'last_name', 'middle_name', 'phone', 'note']


class ReceptionDetail(DetailView):
    model = Reception

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['diagnosis'] = self.get_object().diagnosis.all()
        context['procedures'] = self.get_object().procedure.all()
        return context


class ReceptionCreate(CreateView):
    model = Reception
    fields = ['patient', 'date', 'diagnosis', 'procedure', 'note']

    def form_valid(self, form):
        form.instance.doctor = self.request.user
        return super(ReceptionCreate, self).form_valid(form)
