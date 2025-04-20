from django.db import models
from datetime import timedelta, datetime

class Doctor(models.Model):
    """Модель врача"""
    name = models.CharField(max_length=100, verbose_name="ФИО врача")
    specialization = models.CharField(max_length=100, verbose_name="Специализация")

    def __str__(self):
        return f"{self.name} ({self.specialization})"

class Patient(models.Model):
    """Модель пациента (без привязки к пользователю)"""
    name = models.CharField(max_length=100, verbose_name="ФИО пациента")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")

    def __str__(self):
        return self.name

class Appointment(models.Model):
    """Модель записи на приём"""
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Пациент")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Врач")
    date = models.DateField(verbose_name="Дата приёма")
    time = models.TimeField(verbose_name="Время приёма")
    end_time = models.TimeField(verbose_name="Конец приёма", editable=False)  # Автоматическое поле

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        # Одна запись на врача в определённое время
        unique_together = ['doctor', 'date', 'time']  

    def save(self, *args, **kwargs):
        # Автоматически устанавливаем end_time (время окончания)
        if not self.end_time:
            self.end_time = (datetime.combine(
                datetime.today(), 
                self.time
            ) + timedelta(hours=1)).time()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.patient} → {self.doctor} ({self.date} {self.time})"