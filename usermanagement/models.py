from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    user = models.OneToOneField(User,
                                related_name='patient',
                                )

class Employee(models.Model):
    user = models.OneToOneField(User,
                                related_name='employee',
                                )

    contact_phone = models.CharField(max_length=15, unique=True)
