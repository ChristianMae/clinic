from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppointmentModelViewSet

router = DefaultRouter()
router.register(r'', AppointmentModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
