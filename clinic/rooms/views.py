from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import RoomSerializer


class RoomModelViewSet(ModelViewSet):
    serializer_class = RoomSerializer
    queryset = serializer_class.Meta.model.objects.all()
