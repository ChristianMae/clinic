from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Staff

admin.site.register(Staff, SimpleHistoryAdmin)
