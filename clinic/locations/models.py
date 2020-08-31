from django.db import models
from model_utils.models import TimeStampedModel
from simple_history.models import HistoricalRecords
from utility.constants import OPTIONAL


class Location(TimeStampedModel):
    name = models.CharField(max_length=255, **OPTIONAL)
    history = HistoricalRecords()

    def __str__(self):
        return self.name
