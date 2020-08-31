from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientModelViewSet

router = DefaultRouter()
router.register(r'', PatientModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
