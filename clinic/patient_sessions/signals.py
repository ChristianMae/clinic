from django.db.models.signals import post_save, post_save
from django.dispatch          import receiver


class SessionSignal():

    @receiver(post_save, sender='patient_sessions.Session', dispatch_uid='clinic.patient_sessions.models.Session')
    def update_sync(sender, instance, created=None, **kwargs):
        pass