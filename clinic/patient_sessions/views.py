from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)
from .serializers import (
    SessionSerializer,
    AppointmentSessionSerializer
)


class SessionModelViewSet(ModelViewSet):
    serializer_class = SessionSerializer
    queryset = serializer_class.Meta.model.objects.all()


class AppointmentSessionModelViewSet(ModelViewSet):
    queryset = AppointmentSessionSerializer.Meta.model.objects.all()
    serializer_class = AppointmentSessionSerializer
    
    def get_queryset(self):
        model = self.serializer_class.Meta.model
        if not self.kwargs.get('pk'):
            room = self.request.GET.get('room', None)
            machine = self.request.GET.get('machine', None)
            date = self.request.GET.get('date', None)
            sessions = model.objects.filter(room__id=room, machine__id=machine, date=date, status='active')
        else:
            sessions = model.objects.all()
        return sessions
