from rest_framework import serializers
from .models import Doctor, Patient, Appointment
from django.core.exceptions import ValidationError
from datetime import time

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['id', 'name', 'specialization']

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'phone']

class AppointmentSerializer(serializers.ModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all())
    patient = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all())

    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'doctor', 'date', 'time']

    def validate(self, data):
        """Проверка времени записи"""
        time_obj = data['time']
        date_obj = data['date']

        # Проверка что время начинается ровно в час (минуты = 0)
        if time_obj.minute != 0:
            raise serializers.ValidationError("Запись возможна только на начало часа (например, 14:00)")

        # Проверка рабочего времени (9:00-17:00)
        if time_obj < time(9, 0) or time_obj > time(17, 0):
            raise serializers.ValidationError("Поликлиника работает с 9:00 до 18:00. Последний прием в 17:00")

        # Проверка дня недели (пн-пт)
        if date_obj.weekday() >= 5:  # 5=суббота, 6=воскресенье
            raise serializers.ValidationError("Запись возможна только в будни")

        # Проверка что время не занято
        existing = Appointment.objects.filter(
            doctor=data['doctor'],
            date=data['date'],
            time=data['time']
        ).exists()
        
        if existing:
            raise serializers.ValidationError("Это время уже занято")

        return data