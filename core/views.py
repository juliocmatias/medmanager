from rest_framework import viewsets

from .models import Appointment, HealthProfessional
from .serializers import AppointmentSerializer, HealthProfessionalSerializer


class HealthProfessionalViewSet(viewsets.ModelViewSet):
    queryset = HealthProfessional.objects.all()
    serializer_class = HealthProfessionalSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
