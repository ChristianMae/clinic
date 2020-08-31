from rest_framework.serializers import ModelSerializer
from .models import (
    Session,
    AppointmentSession
)


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
        instance.time = validated_data.get('time', instance.time)
        instance.symptoms = validated_data.get('symptoms', instance.symptoms)
        instance.findings = validated_data.get('findings', instance.findings)
        instance.prescription = validated_data.get('prescription', instance.prescription)
        instance.image = validated_data.get('image', instance.image)
        return instance
