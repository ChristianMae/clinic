from rest_framework.serializers import ModelSerializer
from .models import Appointment


class AppointmentSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.patient = validated_data.get('patient', instance.patient)
        instance.date = validated_data.get('date', instance.date)
        instance.time = validated_data.get('time', instance.time)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance

