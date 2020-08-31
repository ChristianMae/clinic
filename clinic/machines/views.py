from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import MachineSerializer


class MachineModelViewSet(ModelViewSet):
    serializer_class = MachineSerializer
    queryset = serializer_class.Meta.model.objects.all()
