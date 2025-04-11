import re

from django.utils import timezone
from rest_framework import serializers

from .models import Appointment, HealthProfessional


class HealthProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProfessional
        fields = "__all__"

    def validate_social_name(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError("O nome social é obrigatório.")
        if len(value) < 3:
            raise serializers.ValidationError(
                "O nome social deve ter pelo menos 3 caracteres."
            )

        existing = HealthProfessional.objects.filter(social_name__iexact=value)
        if self.instance:
            existing = existing.exclude(pk=self.instance.pk)

        if existing.exists():
            raise serializers.ValidationError(
                "Já existe um profissional com esse nome social."
            )

        return value

    def validate_specialty(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("A especialidade é obrigatória.")
        return value

    def _clean_phone(self, value):
        return re.sub(r"\D", "", value)

    def validate_phone(self, value):
        if not value:
            raise serializers.ValidationError("O telefone é obrigatório.")

        if any(char.isalpha() for char in value):
            raise serializers.ValidationError("Número de telefone inválido.")

        cleaned = self._clean_phone(value)

        if len(cleaned) < 10 or len(cleaned) > 11:
            raise serializers.ValidationError("Número de telefone inválido.")

        # Verificar duplicidade diretamente no Python
        existing = HealthProfessional.objects.all()
        for professional in existing:
            existing_cleaned = self._clean_phone(professional.phone)
            if existing_cleaned == cleaned and (
                not self.instance or professional.pk != self.instance.pk
            ):
                raise serializers.ValidationError("O número de telefone já existe.")

        return value

    def create(self, validated_data):
        validated_data["phone"] = self._clean_phone(validated_data["phone"])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if "phone" in validated_data:
            validated_data["phone"] = self._clean_phone(validated_data["phone"])
        return super().update(instance, validated_data)


class AppointmentSerializer(serializers.ModelSerializer):
    professional = serializers.PrimaryKeyRelatedField(
        queryset=HealthProfessional.objects.all()
    )

    class Meta:
        model = Appointment
        fields = "__all__"

    def validate_appointment_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError(
                "A data da consulta não pode estar no passado."
            )
        return value

    def validate(self, data):
        professional = data.get("professional")
        appointment_date = data.get("appointment_date")

        existing_appointments = Appointment.objects.filter(
            professional=professional, appointment_date=appointment_date
        )
        if self.instance:
            existing_appointments = existing_appointments.exclude(pk=self.instance.pk)

        if existing_appointments.exists():
            raise serializers.ValidationError(
                "Este profissional já possui uma consulta marcada neste horário."
            )

        return data
