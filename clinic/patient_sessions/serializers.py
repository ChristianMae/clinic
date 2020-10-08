from datetime import timedelta
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ValidationError
)
from .models import (
    Session,
    AppointmentSession
)
from clinic.rooms.models import Room
from clinic.patients.models import Patient
from clinic.machines.models import Machine
from clinic.patients.serializers import PatientSerializer
from utility.utils import date_offset_generator


class AppointmentSessionSerializer(ModelSerializer):
    machine_name = SerializerMethodField()
    room_name = SerializerMethodField()
    client_name = SerializerMethodField()
    client_id = SerializerMethodField()

    class Meta:
        model = AppointmentSession
        fields = '__all__'

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.session = validated_data.get('session', instance.session)
        instance.status = validated_data.get('status', instance.status)
        instance.room = validated_data.get('room', instance.room)
        instance.machine = validated_data.get('machine', instance.machine)
        instance.date = validated_data.get('date', instance.date)
        instance.machine_start_time = validated_data.get('machine_start_time', instance.machine_start_time)
        instance.machine_end_time = validated_data.get('machine_end_time', instance.machine_end_time)
        instance.room_start_time = validated_data.get('room_start_time', instance.room_start_time)
        instance.room_end_time = validated_data.get('room_end_time', instance.room_end_time)
        instance.symptoms = validated_data.get('symptoms', instance.symptoms)
        instance.findings = validated_data.get('findings', instance.findings)
        instance.prescription = validated_data.get('prescription', instance.prescription)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance
    
    def get_machine_name(self,obj):
        try:
            return '{0}'.format(obj.machine.name)
        except:
            return '-'
        
    
    def get_room_name(self,obj):
        try:
            return '{0}'.format(obj.room.room_no)
        except:
            return '-'
    
    def get_client_name(self,obj):
        try:
            return '{0} {1}'.format(obj.session.patient.first_name,obj.session.patient.last_name)
        except:
            return '-'
    
    def get_client_id(self,obj):
        try:
            return '{0}'.format(obj.session.patient.id)
        except:
            return '-'


class SessionSerializer(ModelSerializer):
    sessions = AppointmentSessionSerializer(many=True, read_only=True)
    patient = SerializerMethodField()
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
        patient_id = self.initial_data['patient']
        try:
            patient = Patient.objects.get(pk=patient_id)
        except Patient.DoesNotExist:
            raise ValidationError(f'Patient with id {patient_id} does not exist.')
        session_detail = self.Meta.model.objects.create(patient=patient, **validated_data)
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
        instance.save()
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

    def get_patient(self, obj):
        return f'{obj.patient.first_name} {obj.patient.last_name}'
