from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import AppointmentSerializer


class AppointmentModelViewSet(ModelViewSet):
    serializer_class = AppointmentSerializer
    queryset = serializer_class.Meta.model.objects.all()
