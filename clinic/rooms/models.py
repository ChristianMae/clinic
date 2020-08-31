from django.db import models
from model_utils.models import TimeStampedModel
from simple_history.models import HistoricalRecords
from utility.constants import OPTIONAL


class Room(TimeStampedModel):
    room_no = models.CharField(max_length=3)
    floor_no = models.CharField(max_length=3)
    location = models.ForeignKey('locations.Location', on_delete=models.CASCADE, related_name='location', **OPTIONAL)
    history = HistoricalRecords()
    
    def __str__(self):
        return f'{self.location} - {self.room_no}'