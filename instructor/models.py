from django.contrib.auth.models import User
from django.db import models


class Medicine(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Medikament')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Medisin'
        verbose_name_plural = 'Medisiner'


class Medium(models.Model):
    UNITS = (
        (0, 'mg'),
        (1, 'mg/ml'),
        (2, ' - ')
    )

    medicine = models.ForeignKey(Medicine)
    size = models.PositiveSmallIntegerField()
    unit = models.PositiveSmallIntegerField(choices=UNITS)

    def __str__(self):
        return f'{self.medicine} - {self.size} [{self.get_unit_display()}]'

    class Meta:
        verbose_name = 'Medisinenhet'
        verbose_name_plural = 'Medisinenheter'


class Disease(models.Model):
    title = models.CharField(max_length=200,
                             verbose_name='Sykdom')
    medicines = models.ForeignKey(Medicine,
                                  related_name='diseases',
                                  verbose_name='Medikamenter')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Sykdom'
        verbose_name_plural = 'Sykdommer'


class Plan(models.Model):  # Nedtrappingsplan - generell - denne velger legen
    """slooope bratt"""
    title = models.CharField(max_length=100,
                             verbose_name='Tittel')
    comment = models.TextField(verbose_name='Kommentar')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Nedtrappingsplan'
        verbose_name_plural = 'Nedtrappingsplaner'


class Dosage(models.Model):
    amount = models.DecimalField(max_digits=6,
                                 decimal_places=2,
                                 verbose_name='Dose')

    class Meta:
        abstract = True


class PlanDosage(Dosage):
    """ Single dose for a given point in a plan """
    plan = models.ForeignKey(Plan)
    offset = models.DurationField()

    class Meta:
        verbose_name = 'Dose'
        verbose_name_plural = 'Doser'


class PatientTreatmentPlan(models.Model):  # Spesifikk pasient "planoversikt"
    plan = models.ForeignKey(Plan)
    patient = models.ForeignKey(User, related_name='plan')
    author = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    start = models.DateTimeField()
    edited = models.DateTimeField(auto_now=True)
    comment = models.TextField()
    medicine = models.ForeignKey(Medicine)
    disease = models.ForeignKey(Disease)

    class Meta:
        verbose_name = 'Pasient behandlingsplan'
        verbose_name_plural = 'Pasient behandlingsplaner'


class UserDose(Dosage):
    offset = models.DurationField()
    treatment_plan = models.ForeignKey(PatientTreatmentPlan)
    taken = models.DecimalField(max_digits=6,
                                decimal_places=2,
                                blank=True,
                                null=True)

    def discrepancy(self):
        if self.taken:
            return self.amount - self.taken
        else:
            return self.amount

    class Meta:
        verbose_name = 'Pasientdose'
        verbose_name_plural = 'Pasientdoser'
