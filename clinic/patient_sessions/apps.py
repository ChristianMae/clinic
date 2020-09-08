from django.apps import AppConfig


class PatientSessionsConfig(AppConfig):
    name = 'clinic.patient_sessions'

    def ready(self):
        from .signals import SessionSignal
