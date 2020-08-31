from django.db import models
from model_utils.models import TimeStampedModel
from simple_history.models import HistoricalRecords
from utility.constants import OPTIONAL


class Appointment(TimeStampedModel):
    """
    Contains all the first time appointment and consultations only
    """
    patient = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, related_name='patients', **OPTIONAL)
    date = models.DateField(**OPTIONAL)
    time = models.TimeField(**OPTIONAL)
    location = models.ForeignKey('locations.Location', on_delete=models.CASCADE, **OPTIONAL)
    history = HistoricalRecords()

    def __str__(self):
        return self.patient