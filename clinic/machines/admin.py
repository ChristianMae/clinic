from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Machine

admin.site.register(Machine, SimpleHistoryAdmin)
