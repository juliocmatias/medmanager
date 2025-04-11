import pytest
from django.utils import timezone
from rest_framework.test import APIClient
from core.models import Appointment, HealthProfessional
from datetime import timedelta


@pytest.mark.django_db
def test_create_valid_appointment():
    professional = HealthProfessional.objects.create(
        social_name="Dr. Ricardo", specialty="Neurologia", phone="11955555555"
    )
    client = APIClient()
    payload = {
        "professional": professional.id,
        "appointment_date": (timezone.now() + timedelta(days=1)).isoformat(),
    }
    response = client.post("/api/appointments/", data=payload, format="json")
    assert response.status_code == 201
    assert Appointment.objects.filter(professional=professional).exists()


@pytest.mark.django_db
def test_create_appointment_with_nonexistent_professional():
    client = APIClient()
    payload = {
        "professional": 999,  # ID inexistente
        "appointment_date": (timezone.now() + timedelta(days=2)).isoformat(),
    }
    response = client.post("/api/appointments/", data=payload, format="json")
    assert response.status_code == 400
    assert "professional" in response.data


@pytest.mark.django_db
def test_create_appointment_missing_date():
    professional = HealthProfessional.objects.create(
        social_name="Dra. Bianca", specialty="Dermatologia", phone="11944444444"
    )
    client = APIClient()
    payload = {
        "professional": professional.id,
        # falta o campo appointment_date
    }
    response = client.post("/api/appointments/", data=payload, format="json")
    assert response.status_code == 400
    assert "appointment_date" in response.data


@pytest.mark.django_db
def test_create_appointment_missing_professional():
    client = APIClient()
    payload = {
        # falta o campo professional
        "appointment_date": (timezone.now() + timedelta(days=2)).isoformat()
    }
    response = client.post("/api/appointments/", data=payload, format="json")
    assert response.status_code == 400
    assert "professional" in response.data


@pytest.mark.django_db
def test_create_appointment_with_invalid_date_format():
    professional = HealthProfessional.objects.create(
        social_name="Dr. Fábio", specialty="Endocrinologia", phone="11922222222"
    )
    client = APIClient()
    payload = {
        "professional": professional.id,
        "appointment_date": "amanhã às 10h",  # formato inválido
    }
    response = client.post("/api/appointments/", data=payload, format="json")
    assert response.status_code == 400
    assert "appointment_date" in response.data
