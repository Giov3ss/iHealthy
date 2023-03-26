from django import forms
from .models import Appointment
from django.contrib.auth.models import User


class AppointmentForm(forms.ModelForm):

    def __init__(self, user_id, *args, **kwargs):
        self.user_id = user_id
        super(AppointmentForm, self).__init__(*args, **kwargs)

    def clean(self):
        super().clean()
        self.instance.user_id = self.user_id

    class Meta:
        model = Appointment
        fields = [
            'date',
            'time',
            'location',
            'reason',
        ]

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'})
        }
