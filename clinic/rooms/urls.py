from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoomModelViewSet

router = DefaultRouter()
router.register(r'', RoomModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
