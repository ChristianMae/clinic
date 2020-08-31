from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProcedureModelViewSet

router = DefaultRouter()
router.register(r'', ProcedureModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
]