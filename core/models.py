from django.db import models

# Create your models here.

class HealthProfessional(models.Model):
    social_name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.social_name
    
class Appointment(models.Model):
    professional = models.ForeignKey(HealthProfessional, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.professional} - {self.appointment_date.strftime("%Y-%m-%d %H:%M")}'