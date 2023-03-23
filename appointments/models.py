from django.db import models
from django.contrib.auth.models import User


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.name} - {self.date} - {self.time}'
