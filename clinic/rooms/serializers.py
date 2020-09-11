from rest_framework. serializers import ModelSerializer
from .models import Room


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.room_no = validated_data.get('room_no', instance.room_no)
        instance.floor_no = validated_data.get('floor_no', instance.floor_no)
        instance.location = validated_data.get('location', instance.location)
        instance.save()

        return instance
