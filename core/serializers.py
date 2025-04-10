import re
from rest_framework import serializers
from .models import HealthProfessional, Appointment

class HealthProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProfessional
        fields = '__all__'
    
    def validate_social_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("O nome social é obrigatório.")
        if len(value.strip()) < 3:
            raise serializers.ValidationError("O nome social deve ter pelo menos 3 caracteres.")
        return value
    
    def validate_specialty(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("A especialidade é obrigatória.")
        return value
    
    def validate_phone(self, value):
        if not value:
            raise serializers.ValidationError("O telefone é obrigatório.")

        if re.search(r'[a-zA-Z]', value):
            raise serializers.ValidationError("Número de telefone inválido.")

        cleaned = re.sub(r'\D', '', value)

        if len(cleaned) < 10 or len(cleaned) > 11:
            raise serializers.ValidationError("Número de telefone inválido.")

        return value

class AppointmentSerializer(serializers.ModelSerializer):
    professional = serializers.PrimaryKeyRelatedField(queryset=HealthProfessional.objects.all())

    class Meta:
        model = Appointment
        fields = '__all__'
