from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from . models import Patient, Reception, Diagnosis, Procedure
from django.urls import reverse_lazy
from django.db.models import Q
import datetime


class Index(TemplateView):
    template_name = 'receptions/index.html'


class PatientsList(ListView):
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        if self.request.GET.get('search'):
            self.extra_context = {'search': True}
        return super().get_context_data()

    def get_queryset(self):
        search = self.request.GET.get('search')
        if search is not None:
            return Patient.objects.filter(
                Q(name__startswith=search) |
                Q(last_name__startswith=search) |
                Q(middle_name__startswith=search)
            )
        return Patient.objects.all()


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
    paginate_by = 10

    def get_queryset(self):
        date = self.request.GET.get('search')
        if date:
            date = datetime.datetime.strptime(date, '%Y-%m-%d')
            return self.request.user.receptions.filter(date__day=date.day, date__month=date.month, date__year=date.year)
        date_from = self.request.GET.get('search_from')
        date_to = self.request.GET.get('search_to')
        if date_from or date_to:
            if date_from:
                date_from = datetime.datetime.strptime(date_from, '%Y-%m-%d')
                if date_to:
                    date_to = datetime.datetime.strptime(date_to, '%Y-%m-%d')
                    return self.request.user.receptions.filter(Q(date__gte=date_from) & Q(date__lte=date_to))
                else:
                    return self.request.user.receptions.filter(date__gte=date_from)
            else:
                date_to = datetime.datetime.strptime(date_to, '%Y-%m-%d')
                return self.request.user.receptions.filter(date__lte=date_to)
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

    def get_initial(self):
        patient = self.request.GET.get('patient')
        initial = super().get_initial()
        if patient:
            initial.update({'patient': patient})
        return initial

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
    paginate_by = 10

    def get_queryset(self):
        search = self.request.GET.get('search')
        if search is not None:
            return Diagnosis.objects.filter(text__contains=search)
        return Diagnosis.objects.all()


class DiagnosisCreate(CreateView):
    model = Diagnosis
    fields = ['text']
    success_url = reverse_lazy('receptions:diagnoses')


class DiagnosisUpdate(UpdateView):
    model = Diagnosis
    fields = ['text']
    success_url = reverse_lazy('receptions:diagnoses')


class DiagnosisDelete(DeleteView):
    model = Diagnosis
    success_url = reverse_lazy('receptions:diagnoses')


class ProcedureList(ListView):
    paginate_by = 10

    def get_queryset(self):
        search = self.request.GET.get('search')
        if search is not None:
            return Procedure.objects.filter(text__contains=search)
        return Procedure.objects.all()


class ProcedureCreate(CreateView):
    model = Procedure
    fields = ['text']
    success_url = reverse_lazy("receptions:procedures")


class ProcedureUpdate(UpdateView):
    model = Procedure
    fields = ['text']
    success_url = reverse_lazy("receptions:procedures")


class ProcedureDelete(DeleteView):
    model = Procedure
    success_url = reverse_lazy('receptions:procedures')
