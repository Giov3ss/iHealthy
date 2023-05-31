import datetime
from django import forms
from django.core.exceptions import ValidationError
from .models import Appointment
from django.contrib.auth.models import User


class DateInput(forms.DateInput):
    """
    This class gets the widget working to show a datepicker
    """
    input_type = 'date'


class TimeInput(forms.TimeInput):
    """
    This class gets the widget working to show a datepicker
    """
    input_type = 'text'


class AppointmentForm(forms.ModelForm):
    """
    Form for creating and updating an appointment.

    Attributes:
        - user_id (int): The ID of the user associated with the appointment.

    Methods:
        - __init__(user_id, *args, **kwargs): Initializes the form instance.
        - clean(): Performs form validation and cleans the form data.
    """

    def __init__(self, user_id, *args, **kwargs):
        """
        Initializes the form instance.

        """
        self.user_id = user_id
        super(AppointmentForm, self).__init__(*args, **kwargs)

    def clean(self):
        """
        Performs form validation and cleans the form data.
        Checks for conflicts with existing appointments and validates the date.

        Raises:
            - forms.ValidationError: If there is a conflict with an existing appointment or date is in the past.  # noqa

        """
        super().clean()
        self.instance.user_id = self.user_id
        date = self.cleaned_data.get("date")
        time = self.cleaned_data.get("time")
        nutritionist = self.cleaned_data.get('nutritionist')
        conflicts = Appointment.objects.filter(date=date).filter(time=time).filter(nutritionist=nutritionist).exclude(pk=self.instance.pk)  # noqa
        if conflicts.exists():
            raise forms.ValidationError("This appointment conflicts with an existing appointment.")  # noqa
        if date < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")

    class Meta:
        model = Appointment
        fields = [
            'date',
            'time',
            'reason',
            'nutritionist',
        ]

        widgets = {
            'date': DateInput(attrs={
                'min': datetime.date.today() + datetime.timedelta(days=0),
                'max': datetime.date.today() + datetime.timedelta(days=30)
            }),
            'time': TimeInput(attrs={
                'class': 'timepicker'
            }),
            'nutritionist': forms.Select(attrs={'class': 'form-select'}),
        }
