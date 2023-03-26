from django.shortcuts import render, get_object_or_404, redirect
from ..models import Appointment
from ..forms import AppointmentForm
from django.contrib.auth.decorators import login_required


@login_required
def list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments/list.html', {'appointments': appointments})  # noqa


@login_required
def detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'appointments/detail.html', {'appointment': appointment})  # noqa


@login_required
def create(request):
    form = AppointmentForm(request.user.id, request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('appointment_list')
    return render(request, 'appointments/form.html', {'form': form, 'title': 'create'})  # noqa


@login_required
def update(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    form = AppointmentForm(request.POST or None, instace=appointment)
    if form.is_valid():
        form.save()
        return redirect('appointment_list')
    return render(request, 'appointments/form.html', {'form': form, 'title': 'update'})  # noqa


@login_required
def delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'appointments/appointment_delete.html')

