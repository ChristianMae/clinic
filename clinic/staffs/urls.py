from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StaffModelViewSet

router = DefaultRouter()
router.register(r'', StaffModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
