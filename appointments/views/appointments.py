from django.shortcuts import render, get_object_or_404
from .models import User, Appointment


def appointment_list(request):
    appointment = Appointment.objects.all()
    return render(request, 'appointments/appointment_list.html', {'appointment': appointment})  # noqa


def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'appointments/appointment_detail.html', {'appointments': appointment})  # noqa


def user_list(request):
    users = User.objects.all()
    return render(request, 'appointments/user_list.html', {'users': users})  # noqa


def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'appointments/user_detail.html', {'user': user})  # noqa
