from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Procedure

admin.site.register(Procedure, SimpleHistoryAdmin)
