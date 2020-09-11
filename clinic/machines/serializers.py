from rest_framework.serializers import ModelSerializer
from .models import Machine


class MachineSerializer(ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.model = validated_data.get('model', instance.model)
        instance.save()
        return instance