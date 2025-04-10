from rest_framework import serializers
from .models import HealthProfessional, Appointment

class HealthProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProfessional
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    professional = serializers.PrimaryKeyRelatedField(queryset=HealthProfessional.objects.all())

    class Meta:
        model = Appointment
        fields = '__all__'
