from rest_framework import generics
from .models import Doctor, Patient, Appointment
from .serializers import DoctorSerializer, AppointmentSerializer, PatientSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Список врачей + детали одного врача
class DoctorList(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorDetail(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

# Список пациентов + детали
class PatientList(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

# Записи: просмотр, создание, отмена
class AppointmentList(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['doctor', 'date']

class AppointmentDetail(generics.RetrieveDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer