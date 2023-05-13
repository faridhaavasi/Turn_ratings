from django.contrib import admin
from . models import Turn, Mont, Hour, Time
# Register your models here.

admin.site.register(Turn)
admin.site.register(Time)
admin.site.register(Mont)
admin.site.register(Hour)