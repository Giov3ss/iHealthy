import datetime
from django import forms
from django.core.exceptions import ValidationError
from .models import Appointment
from django.contrib.auth.models import User


class AppointmentForm(forms.ModelForm):

    def __init__(self, user_id, *args, **kwargs):
        self.user_id = user_id
        super(AppointmentForm, self).__init__(*args, **kwargs)

    def clean(self):
        super().clean()
        self.instance.user_id = self.user_id
        date = self.cleaned_data.get("date")
        time = self.cleaned_data.get("time")
        nutricionist = self.cleaned_data.get('nutricionist')
        conflicts = Appointment.objects.filter(date=date).filter(time=time).filter(nutricionist=nutricionist).exclude(pk=self.instance.pk)  # noqa
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
            'nutricionist',
        ]

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'nutricionist': forms.Select(attrs={'class': 'form-select'}),
        }
