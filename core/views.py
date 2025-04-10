from rest_framework import viewsets
from .models import HealthProfessional, Appointment
from .serializers import HealthProfessionalSerializer, AppointmentSerializer

class HealthProfessionalViewSet(viewsets.ModelViewSet):
    queryset = HealthProfessional.objects.all()
    serializer_class = HealthProfessionalSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer