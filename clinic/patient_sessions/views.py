from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import (
    SessionSerializer,
    AppointmentSessionSerializer
)


class SessionModelViewSet(ModelViewSet):
    serializer_class = SessionSerializer
    queryset = serializer_class.Meta.model.objects.all()


class AppointmentSessionModelViewSet(ModelViewSet):
    serializer_class = AppointmentSessionSerializer
    queryset = serializer_class.Meta.model.objects.all()
