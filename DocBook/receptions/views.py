from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from . models import Patient, Reception, Diagnosis, Procedure
from django.urls import reverse_lazy


class Index(TemplateView):
    template_name = 'receptions/index.html'


class PatientsList(ListView):
    model = Patient


class PatientDetail(DetailView):
    model = Patient

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['receptions'] = user.receptions.filter(patient=self.get_object())
        return context


class PatientCreate(CreateView):
    model = Patient
    fields = ['name', 'last_name', 'middle_name', 'phone', 'note']


class PatientUpdate(UpdateView):
    model = Patient
    fields = ['name', 'last_name', 'middle_name', 'phone', 'note']


class ReceptionsList(ListView):
    def get_queryset(self):
        return self.request.user.receptions.all()


class ReceptionDetail(DetailView):
    def get_queryset(self):
        return self.request.user.receptions.all()

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


class ReceptionUpdate(UpdateView):
    fields = ['patient', 'date', 'diagnosis', 'procedure', 'note']

    def get_queryset(self):
        return self.request.user.receptions.all()


class ReceptionDelete(DeleteView):
    success_url = reverse_lazy('receptions:receptions')

    def get_queryset(self):
        return self.request.user.receptions.all()


class DiagnosisList(ListView):
    model = Diagnosis


class DiagnosisCreate(CreateView):
    model = Diagnosis
    fields = ['text']


class DiagnosisUpdate(UpdateView):
    model = Diagnosis
    fields = ['text']


class DiagnosisDelete(DeleteView):
    model = Diagnosis
    success_url = reverse_lazy('receptions:diagnoses')


class ProcedureList(ListView):
    model = Procedure


class ProcedureCreate(CreateView):
    model = Procedure
    fields = ['text']


class ProcedureUpdate(UpdateView):
    model = Procedure
    fields = ['text']


class ProcedureDelete(DeleteView):
    model = Procedure
    success_url = reverse_lazy('receptions:procedures')
