from django.shortcuts import render, get_object_or_404
from ..models import Appointment
from ..forms import AppointmentForm


def list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments/list.html', {'appointments': appointments})  # noqa


def detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'appointments/detail.html', {'appointment': appointment})  # noqa


def create(request):
    form = AppointmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('appointment_list')
    return render(request, 'appointments/form.html', {'form': form})


def update(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    form = AppointmentForm(request.POST or None, instace=appointment)
    if form.is_valid():
        form.save()
        return redirect('appointment_list')
    return render(request, 'appointments/form.html', {'form': form})


def delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'appointments/appointment_delete.html')

