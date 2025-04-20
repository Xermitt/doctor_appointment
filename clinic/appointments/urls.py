from django.urls import path

from .views import (
    DoctorList, DoctorDetail,
    PatientList,
    AppointmentList, AppointmentDetail
)

urlpatterns = [
    path('doctors/', DoctorList.as_view()),
    path('doctors/<int:pk>/', DoctorDetail.as_view()),
    path('patients/', PatientList.as_view()),
    path('appointments/', AppointmentList.as_view()),
    path('appointments/<int:pk>/', AppointmentDetail.as_view()),
]