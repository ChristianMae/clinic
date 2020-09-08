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
    serializer_class = AppointmentSessionSerializer
    queryset = serializer_class.Meta.model.objects.all()


class CreateSessionAPIView(CreateAPIView):
    serializer_class = AppointmentSessionSerializer
