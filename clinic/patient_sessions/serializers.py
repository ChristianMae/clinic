import calendar
from datetime import timedelta
from rest_framework.serializers import (ModelSerializer, SerializerMethodField)
from .models import (
    Session,
    AppointmentSession
)
from clinic.rooms.models import Room
from clinic.machines.models import Machine
from clinic.patients.serializers import PatientSerializer


class AppointmentSessionSerializer(ModelSerializer):

    class Meta:
        model = AppointmentSession
        fields = ('__all__')

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.session = validated_data.get('session', instance.session)
        instance.status = validated_data.get('status', instance.status)
        instance.room = validated_data.get('room', instance.room)
        instance.machine = validated_data.get('machine', instance.machine)
        instance.date = validated_data.get('date', instance.date)
        instance.time = validated_data.get('time', instance.time)
        instance.symptoms = validated_data.get('symptoms', instance.symptoms)
        instance.findings = validated_data.get('findings', instance.findings)
        instance.prescription = validated_data.get('prescription', instance.prescription)
        instance.image = validated_data.get('image', instance.image)
        return instance


def date_offset_generator(date):
    days_available = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    if calendar.day_name[date.weekday()] in days_available:
        return date
    elif calendar.day_name[date.weekday()] == 'Sunday':
        return date + timedelta(days=1)
    else:
        return date + timedelta(days=2)


class SessionSerializer(ModelSerializer):
    sessions = AppointmentSessionSerializer(many=True, read_only=True)
    class Meta:
        model = Session
        fields = (
            'patient',
            'procedure',
            'session_interval',
            'number_of_session',
            'start_date',
            'sessions'
        )

    def create(self, validated_data):
        session_detail = self.Meta.model.objects.create(**validated_data)
        sessions = self.generate_sessions(session=session_detail)
        for session in sessions:
            AppointmentSession.objects.create(session=session_detail, status='active', **session)
        return session_detail

    def update(self, instance, validated_data):
        instance.patient = validated_data.get('patient', instance.patient)
        instance.procedure = validated_data.get('procedure', instance.procedure)
        instance.session_interval = validated_data.get('session_interval', instance.session_interval)
        instance.number_of_session = validated_data.get('number_of_session', instance.number_of_session)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        return instance

    def generate_sessions(self, *args, **kwargs):
        session = kwargs.get('session')
        start_date = date_offset_generator(session.start_date)
        sessions = []   
        for counter in range(session.number_of_session):
            date = start_date if counter < 1 else date_offset_generator(date + timedelta(days=int(session.session_interval)))
            data = {
                'date': date
            }
            sessions.append(data)
        return sessions
