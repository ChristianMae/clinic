from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SessionModelViewSet,
    AppointmentSessionModelViewSet
)

router = DefaultRouter()
router.register(r'', SessionModelViewSet)
router.register(r'appointment', AppointmentSessionModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
