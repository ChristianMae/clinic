from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SessionModelViewSet,
    AppointmentSessionModelViewSet
)

session_router = DefaultRouter()
sessions_router = DefaultRouter()
session_router.register(r'session', SessionModelViewSet)
sessions_router.register(r'session_appointment', AppointmentSessionModelViewSet)


urlpatterns = [
    path('', include(session_router.urls)),
    path('', include(sessions_router.urls)),
]
