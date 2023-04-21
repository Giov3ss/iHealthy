from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    
    class Reason(models.TextChoices):
        weight_loss = 'WL', _('Weight Loss')
        weight_gain = 'WG', _('Weight Gain')
        better_healthy = 'BH', _('Better Healthy')
        meal_plan = 'MP', _('Meal Planing')
        nutrition_education = 'NE', _('Nutrition Education')
        other = 'OT', _('Other')

    reason = models.CharField(
        max_length=2,
        choices=Reason.choices,
        default=Reason.weight_loss,
    )

    class Nutricionist(models.TextChoices):
        ANNA = 'Anna', _('Anna Smith')
        JOHN = 'John', _('John Doe')

    nutricionist = models.CharField(
        max_length=4, 
        choices=Nutricionist.choices,
        default=Nutricionist.ANNA,
        )

    def __str__(self):
        return f'{self.date} - {self.time} ({self.nutricionist})'
