from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import (
    Session,
    AppointmentSession
)

admin.site.register(Session, SimpleHistoryAdmin)
admin.site.register(AppointmentSession, SimpleHistoryAdmin)
