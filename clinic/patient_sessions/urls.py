from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    SessionModelViewSet,
    CreateSessionAPIView,
    AppointmentSessionModelViewSet
)

# router = DefaultRouter()
# router.register(r'', SessionModelViewSet)
# router.register(r'session_appointment', AppointmentSessionModelViewSet)


urlpatterns = [
    # path('', include(router.urls)),
    path('', CreateSessionAPIView.as_view())
]
