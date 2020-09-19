from django.db import models
from model_utils.models import TimeStampedModel
from simple_history.models import HistoricalRecords
from utility.constants import OPTIONAL


class Session(TimeStampedModel):
    """
    Contains all the sessions of the patients on each procedure to be apply
    """
    patient = models.ForeignKey(
        'patients.Patient',
        on_delete=models.CASCADE,
        related_name='patient_sessions',
        **OPTIONAL
    )
    procedure = models.ForeignKey(
        'procedures.Procedure',
        on_delete=models.CASCADE,
        related_name='procedures',
        **OPTIONAL
    )
    session_interval = models.CharField(
        max_length=3,
        **OPTIONAL
    )
    number_of_session = models.IntegerField(**OPTIONAL)
    start_date = models.DateField(**OPTIONAL)
    history = HistoricalRecords()

    def __str__(self):
        return f'{self.patient} - {self.procedure}'


class AppointmentSession(TimeStampedModel):
    ACTIVE = 'active'
    DONE = 'done'
    CANCELED = 'cancel'
    RESCHEDULE = 'reschedule'
    APPOINTMENT_STATUS = [
        (ACTIVE, 'active'),
        (DONE, 'done'),
        (CANCELED, 'canceled'),
        (RESCHEDULE, 'reschedule')
    ]

    session = models.ForeignKey(
        'patient_sessions.Session',
        on_delete=models.CASCADE,
        related_name='sessions',
        **OPTIONAL
    )
    status = models.CharField(
        max_length=10,
        choices=APPOINTMENT_STATUS,
        default=ACTIVE,
        **OPTIONAL
    )
    room = models.ForeignKey(
        'rooms.Room',
        on_delete=models.CASCADE,
        related_name='rooms',
        **OPTIONAL
    )
    machine = models.ForeignKey(
        'machines.Machine',
        on_delete=models.CASCADE,
        related_name='machines',
        **OPTIONAL
    )
    date = models.DateField(**OPTIONAL)
    start_time = models.TimeField(**OPTIONAL)
    end_time = models.TimeField(**OPTIONAL)
    symptoms = models.TextField(**OPTIONAL)
    findings = models.TextField(**OPTIONAL)
    prescription = models.TextField(**OPTIONAL)
    image = models.ImageField(**OPTIONAL)
    history = HistoricalRecords()


    def __str__(self):
        try:
            return f'{self.session.patient} - {self.date}'
        except:
            return '-'
        
