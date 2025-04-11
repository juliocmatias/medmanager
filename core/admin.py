from django.contrib import admin

from core.models import Appointment, HealthProfessional

# Register your models here.
admin.site.register(HealthProfessional)
admin.site.register(Appointment)
