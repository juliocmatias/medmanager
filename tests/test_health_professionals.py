import pytest
from rest_framework.test import APIClient
from core.models import HealthProfessional


@pytest.mark.django_db
def test_create_health_professional_with_empty_name():
    client = APIClient()
    payload = {
        "social_name": " ",
        "specialty": "Psicologia",
        "phone": "11999999999",
    }
    response = client.post("/api/professionals/", data=payload, format="json")
    assert response.status_code == 400
    assert "social_name" in response.data


@pytest.mark.django_db
def test_create_health_professional_with_short_name():
    client = APIClient()
    payload = {
        "social_name": "Jo",
        "specialty": "Psicologia",
        "phone": "11999999999",
    }
    response = client.post("/api/professionals/", data=payload, format="json")
    assert response.status_code == 400
    assert "social_name" in response.data


@pytest.mark.django_db
def test_create_health_professional_with_duplicate_name():
    HealthProfessional.objects.create(
        social_name="Dr. João", specialty="Psiquiatria", phone="11988888888"
    )
    client = APIClient()
    payload = {
        "social_name": "dr. joão",
        "specialty": "Psiquiatria",
        "phone": "11999999999",
    }
    response = client.post("/api/professionals/", data=payload, format="json")
    assert response.status_code == 400
    assert "social_name" in response.data


@pytest.mark.django_db
def test_create_health_professional_with_invalid_phone():
    client = APIClient()
    payload = {
        "social_name": "Dra. Maria",
        "specialty": "Psicologia",
        "phone": "11abc999xyz",
    }
    response = client.post("/api/professionals/", data=payload, format="json")
    assert response.status_code == 400
    assert "phone" in response.data


@pytest.mark.django_db
def test_create_health_professional_with_duplicate_phone():
    HealthProfessional.objects.create(
        social_name="Dra. Luiza", specialty="Fonoaudiologia", phone="11999999999"
    )
    client = APIClient()
    payload = {
        "social_name": "Dra. Ana",
        "specialty": "Fisioterapia",
        "phone": "(11) 99999-9999",
    }
    response = client.post("/api/professionals/", data=payload, format="json")
    assert response.status_code == 400
    assert "phone" in response.data
