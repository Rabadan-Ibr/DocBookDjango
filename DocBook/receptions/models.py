import django.utils.timezone
from django.db import models
from django.contrib.auth import get_user_model

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
        return self.name


class Diagnosis(models.Model):
    text = models.CharField(verbose_name='Диагноз', max_length=200)

    class Meta:
        verbose_name = 'Диагноз'
        verbose_name_plural = 'Диагнозы'

    def __str__(self):
        return self.text[:30]


class Procedure(models.Model):
    text = models.CharField(verbose_name='Лечение', max_length=200)

    class Meta:
        verbose_name = 'Лечение'
        verbose_name_plural = 'Лечения'

    def __str__(self):
        return self.text[:30]


class Reception(models.Model):
    doctor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='receptions',
        blank=True,
        null=True
    )
    patient = models.ForeignKey(
        'Patient',
        on_delete=models.CASCADE,
        related_name='receptions'
    )
    date = models.DateTimeField(
        verbose_name='Дата приема',
        default=django.utils.timezone.now
    )
    diagnosis = models.ManyToManyField(
        'Diagnosis',
        related_name='receptions',
        blank=True
    )
    procedure = models.ManyToManyField(
        'Procedure',
        related_name='receptions',
        blank=True
    )
    note = models.CharField(
        verbose_name='Примичание',
        max_length=256,
        blank=True
    )

    class Meta:
        verbose_name = 'Прием'
        verbose_name_plural = 'Приемы'

    def __str__(self):
        return str(self.patient) + '-' + str(self.date.date())