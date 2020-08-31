from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import LocationSerializer


class LocationModelViewSet(ModelViewSet):
    serializer_class = LocationSerializer
    queryset = serializer_class.Meta.model.objects.all()
