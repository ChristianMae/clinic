"""clinic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

admin.autodiscover()
admin.site.enable_nav_sidebar = False

urlpatterns = [
    path(
        'api/v1/',
        include([
            path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
            path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
            path('location/', include('clinic.locations.urls')),
            path('machine/', include('clinic.machines.urls')),
            path('procedure/', include('clinic.procedures.urls')),
            path('room/', include('clinic.rooms.urls')),
            path('patient/', include('clinic.patients.urls')),
            path('appointment/', include('clinic.appointments.urls')),
            path('staff/', include('clinic.staffs.urls')),
            path('session/', include('clinic.patient_sessions.urls'))
        ])),
    path('admin/', admin.site.urls)
]
