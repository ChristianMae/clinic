from django.contrib.auth.hashers import make_password
from rest_framework. serializers import ModelSerializer
from .models import Staff



class StaffSerializer(ModelSerializer):
    class Meta:
        model = Staff
        exclude = (
            'user_permissions',
            'groups',
            'is_active',
            'is_admin',
            'date_joined',
            'last_login',
            'is_superuser',
            'username'
        )
    
    def validate_password(self, value):
        return make_password(value)

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.middle_name = validated_data.get('middle_name', instance.middle_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.email = validated_data.get('email', instance.email)
        instance.contact_no = validated_data.get('contact_no', instance.contact_no)
        instance.address = validated_data.get('address', instance.address)
        instance.assigned_to = validated_data.get('assigned_to', instance.assigned_to)
        instance.password = validated_data.get('password', instance.password)
        return instance
