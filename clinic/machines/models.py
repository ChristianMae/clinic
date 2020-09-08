from django.db import models
from model_utils.models import TimeStampedModel
from simple_history.models import HistoricalRecords
from utility.constants import OPTIONAL


class Machine(TimeStampedModel):
    name = models.CharField(max_length=50, **OPTIONAL)
    model = models.CharField(max_length=100, **OPTIONAL)
    history = HistoricalRecords()

    def __str__(self):
        return f'{self.name} - {self.model}'
