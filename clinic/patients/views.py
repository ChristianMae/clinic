from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import PatientSerializer


class PatientModelViewSet(ModelViewSet):
    serializer_class = PatientSerializer
    queryset = serializer_class.Meta.model.objects.all()
