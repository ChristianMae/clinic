from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Appointment

admin.site.register(Appointment, SimpleHistoryAdmin)
