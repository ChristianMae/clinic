from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MachineModelViewSet

router = DefaultRouter()
router.register(r'', MachineModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
