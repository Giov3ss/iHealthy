from django import forms
from .models import Appointment
from django.contrib.auth.models import User


class AppointmentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['user'] = forms.ModelChoiceField(queryset=User.objects.filter(id=user.id))  # noqa
        
    class Meta:
        model = Appointment
        fields = [
            'date',
            'time',
            'location',
            'reason',
            'user'
        ]

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'})
        }
