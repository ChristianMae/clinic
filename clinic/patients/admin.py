from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Patient

admin.site.register(Patient, SimpleHistoryAdmin)
