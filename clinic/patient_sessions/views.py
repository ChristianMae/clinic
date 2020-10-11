import datetime
from django.shortcuts import render
from django.db.models import Q
from rest_framework import viewsets, generics, status, decorators, response 
from .serializers import (
    SessionSerializer,
    AppointmentSessionSerializer
)


class SessionModelViewSet(viewsets.ModelViewSet):
    serializer_class = SessionSerializer
    queryset = serializer_class.Meta.model.objects.all()

    def get_queryset(self):
        try:
            return self.serializer_class.Meta.model.objects.filter(patient__id=self.request.GET['patient'])
        except:
            return self.serializer_class.Meta.model.objects.all()
            pass


class AppointmentSessionModelViewSet(viewsets.ModelViewSet):
    queryset = AppointmentSessionSerializer.Meta.model.objects.all()
    serializer_class = AppointmentSessionSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        data = self.get_serializer(queryset,many=True).data

        return response.Response(data, status = status.HTTP_200_OK)

    @decorators.action(detail=True, methods=['get'], name='room_occupied_list')
    def room_occupied_list(self, request, pk=None):
        queryset = self.get_queryset()
        occupied_rooms = queryset.filter(room__id=pk)
        data = self.get_serializer(occupied_rooms, many=True).data

        return response.Response(data, status = status.HTTP_200_OK)

    @decorators.action(detail=True, methods=['get'], name='machine_occcupied_list')
    def machine_occcupied_list(self, request, pk=None):
        queryset = self.get_queryset()
        occupied_machines = queryset.filter(machine__id=pk)
        data = self.get_serializer(occupied_machines, many=True).data

        return response.Response(data, status = status.HTTP_200_OK)
    
    @decorators.action(detail=False, methods=['get'], name='unassigned appointments')
    def unassigned_appointment(self, request, pk=None):
        queryset = self.get_queryset()
        unassigned_appointments = queryset.filter(
            Q(machine_start_time__isnull=True) | Q(machine_end_time__isnull=True) | 
            Q(room_start_time__isnull=True) | Q(room_end_time__isnull=True))
        data = self.get_serializer(unassigned_appointments, many=True).data

        return response.Response(data, status = status.HTTP_200_OK)
    
    @decorators.action(detail=False, methods=['get'], name='assigned appointments')
    def assigned_appointments(self, request, pk=None):
        queryset = self.get_queryset()
        assigned_appointments = queryset.filter(
                date__gte=datetime.datetime.today(),
                machine_start_time__isnull=False, 
                machine_end_time__isnull=False,
                room_start_time__isnull=False, 
                room_end_time__isnull=False
            )
        data = self.get_serializer(assigned_appointments, many=True).data

        return response.Response(data, status = status.HTTP_200_OK)
