from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import StaffSerializer


class StaffModelViewSet(ModelViewSet):
    serializer_class = StaffSerializer
    queryset = serializer_class.Meta.model.objects.all()
