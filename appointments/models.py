from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Appointment(models.Model):
    """
    Model representing an appointment.

    Attributes:
        - user (ForeingKey): The user associated with the appointment.
        - date (DateField): The date of the appointment.
        - time (TimeField): The time of the appointment.
        - reason (CharField): The reason of the appointment.
        - nutritionist (CharField): The assigned nutritionist for the appointment.  # noqa

    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    class Reason(models.TextChoices):
        """
        Choices for the reason of the appointment.

        Each choice consists of a code and human-readable name.

        """
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

    class Nutritionist(models.TextChoices):
        """
        Choices for the assigned nutritionist of the appointment.

        Each choice consists of a code and human-readable name.

        """
        ANNA = 'Anna', _('Anna Smith')
        JOHN = 'John', _('John Doe')

    nutritionist = models.CharField(
        max_length=4,
        choices=Nutritionist.choices,
        default=Nutritionist.ANNA,
        )

    def __str__(self):
        """
        Returns a string representation of the appointment.

        Returns:
            - str: A string representation of the appointment in the format: Date - Time (nutritionist).  # noqa
        """
        return f'{self.date} - {self.time} ({self.nutritionist})'
