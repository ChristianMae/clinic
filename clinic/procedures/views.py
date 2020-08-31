from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import ProcedureSerializer


class ProcedureModelViewSet(ModelViewSet):
    serializer_class = ProcedureSerializer
    queryset = serializer_class.Meta.model.objects.all()
