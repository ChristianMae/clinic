from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import (
    Session,
    AppointmentSession
)
from clinic.rooms.models import Room
from clinic.machines.models import Machine


class SessionSerializer(ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.patient = validated_data.get('patient', instance.patient)
        instance.procedure = validated_data.get('procedure', instance.procedure)
        instance.session_interval = validated_data.get('session_interval', instance.session_interval)
        instance.number_of_session = validated_data.get('number_of_session', instance.number_of_session)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        return instance


class AppointmentSessionSerializer(ModelSerializer):
    session = SessionSerializer()

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

    def validate_session(self, data):
        machine = self.initial_data['machine'] if self.initial_data['machine'] else None
        room = self.initial_data['room'] if self.initial_data['room'] else None
        start_time = self.initial_data['start_time'] if self.initial_data['start_time'] else None
        end_time = self.initial_data['end_time'] if self.initial_data['end_time'] else None
        date = data['start_date']

        machines = self.Meta.model.objects.filter(
            machine=machine,
            date=date,
            start_time__range=(start_time, end_time)
        )

        if machines:
            raise serializers.ValidationError(f'Machine is not available on {date} ({start_time})', code='Unavailble')
        
        rooms = self.Meta.model.objects.filter(
            room=room,
            date=date,
            start_time__range=(start_time, end_time)
        )

        if rooms:
            raise serializers.ValidationError(f'Room is not available on {date} ({start_time})', code='Unavailable')

        session_data = dict(data)
        session, created = Session.objects.get_or_create(**session_data)
        return session
    
    def validate_date(self, data):
        return self.initial_data['session.start_date']
