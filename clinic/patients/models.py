from django.db import models
from model_utils.models import TimeStampedModel
from simple_history.models import HistoricalRecords
from utility.constants  import OPTIONAL


class Patient(TimeStampedModel):
    first_name = models.CharField(max_length=30, **OPTIONAL)
    middle_name = models.CharField(max_length=30, **OPTIONAL)
    last_name = models.CharField(max_length=30, **OPTIONAL)
    age = models.CharField(max_length=3, **OPTIONAL)
    gender = models.CharField(max_length=6, **OPTIONAL)
    occupation = models.CharField(max_length=50, **OPTIONAL)
    contact_no = models.CharField(max_length=11, **OPTIONAL)
    address = models.CharField(max_length=255, **OPTIONAL)
    is_active = models.BooleanField(default=True, **OPTIONAL)
    history = HistoricalRecords()

    def __str__(self):
        return '{}, {} {}'.format(self.last_name, self.first_name, self.middle_name)
