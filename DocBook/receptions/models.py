import django.utils.timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from DocBook.conf import BRANCH_CHOICES

User = get_user_model()


class Patient(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=100)
    last_name = models.CharField(verbose_name='Фамилия', max_length=100)
    middle_name = models.CharField(
        verbose_name='Отчество',
        max_length=100,
        blank=True
    )
    phone = models.DecimalField(
        verbose_name='Номер телефона',
        max_digits=20,
        decimal_places=0
    )
    note = models.CharField(
        verbose_name='Примичание',
        max_length=256,
        blank=True
    )

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'

    def __str__(self):
        return str(self.last_name + ' ' + self.name + ' ' + self.middle_name)

    def get_absolute_url(self):
        return reverse('receptions:patient', kwargs={'pk': self.pk})


class Diagnosis(models.Model):
    text = models.CharField(verbose_name='Диагноз', max_length=200)
    branch = models.CharField(
        verbose_name='Отделение',
        max_length=max(len(branch) for branch, show in BRANCH_CHOICES),
        choices=BRANCH_CHOICES
    )

    class Meta:
        verbose_name = 'Диагноз'
        verbose_name_plural = 'Диагнозы'

    def __str__(self):
        return self.text[:30]

    def get_absolute_url(self):
        return reverse('receptions:update_diagnosis', kwargs={'pk': self.pk})


class Procedure(models.Model):
    text = models.CharField(verbose_name='Лечение', max_length=200)
    branch = models.CharField(
        verbose_name='Отделение',
        max_length=max(len(branch) for branch, show in BRANCH_CHOICES),
        choices=BRANCH_CHOICES
    )

    class Meta:
        verbose_name = 'Лечение'
        verbose_name_plural = 'Лечения'

    def __str__(self):
        return self.text[:30]

    def get_absolute_url(self):
        return reverse('receptions:update_procedure', kwargs={'pk': self.pk})


class Part(models.Model):
    name = models.CharField(
        verbose_name='Объект',
        max_length=100
    )

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'


class DiagnosisPart(models.Model):
    diagnosis = models.ForeignKey(
        Diagnosis,
        on_delete=models.PROTECT,
        related_name='diag_parts'
    )
    part = models.ForeignKey(
        Part,
        on_delete=models.PROTECT,
        related_name='diag_parts'
    )


class ProcedurePart(models.Model):
    procedure = models.ForeignKey(
        Procedure,
        on_delete=models.PROTECT,
        related_name='proc_parts'
    )
    part = models.ForeignKey(
        Part,
        on_delete=models.PROTECT,
        related_name='proc_parts'
    )


class Reception(models.Model):
    doctor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='receptions'
    )
    patient = models.ForeignKey(
        'Patient',
        verbose_name='Пациент',
        on_delete=models.CASCADE,
        related_name='receptions'
    )
    date = models.DateTimeField(
        verbose_name='Дата приема',
        default=django.utils.timezone.now
    )
    diagnosis = models.ManyToManyField(
        DiagnosisPart,
        verbose_name='Диагнозы',
        related_name='receptions',
        blank=True
    )
    procedure = models.ManyToManyField(
        ProcedurePart,
        verbose_name='Процедуры',
        related_name='receptions',
        blank=True
    )
    note = models.TextField(
        verbose_name='Заключение',
        blank=True
    )

    class Meta:
        verbose_name = 'Прием'
        verbose_name_plural = 'Приемы'

    def __str__(self):
        return (
            f'Пациент: {self.patient.last_name}'
            f'{self.patient.name} - {self.date.date()}'
        )

    def get_absolute_url(self):
        return reverse('receptions:reception', kwargs={'pk': self.pk})
