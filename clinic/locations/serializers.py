from rest_framework.serializers import ModelSerializer
from .models import Location


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
