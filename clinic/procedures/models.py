from django.db import models
from model_utils.models import TimeStampedModel
from simple_history.models import HistoricalRecords
from utility.constants import OPTIONAL


class Procedure(TimeStampedModel):
    name = models.CharField(max_length=100, **OPTIONAL)
    description = models.CharField(max_length=299, **OPTIONAL)
    price = models.DecimalField(max_digits=10, decimal_places=2, **OPTIONAL)
    history = HistoricalRecords()
    
    def __str__(self):
        return self.name