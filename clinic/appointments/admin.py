from django.contrib import admin
from .models import Doctor, Patient, Appointment

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date', 'time', 'end_time')