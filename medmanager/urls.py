from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from core.views import AppointmentViewSet, HealthProfessionalViewSet

router = DefaultRouter()
router.register(r"professionals", HealthProfessionalViewSet)
router.register(r"appointments", AppointmentViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
