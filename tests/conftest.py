import pytest
from django.contrib.auth.models import User


@pytest.fixture
def admin_user(db):
    return User.objects.create_superuser("admin", "admin@example.com", "password123")
