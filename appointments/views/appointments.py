from django.shortcuts import render, get_object_or_404, redirect
from ..models import Appointment
from ..forms import AppointmentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.base import TemplateView


@login_required
def list(request):
    appointments = Appointment.objects.filter(user_id=request.user.id)
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
        messages.success(request, 'You have created an appointment!')
        return redirect('appointment_list')
    return render(request, 'appointments/form.html', {'form': form, 'title': 'Create'})  # noqa


@login_required
def update(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    form = AppointmentForm(
        request.user.id,
        request.POST or None,
        instance=appointment
        )
    if appointment.user.id == request.user.id:
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment updated successfully!')
            return redirect('appointment_list')
        return render(request, 'appointments/form.html', {'form': form, 'title': 'Update'})  # noqa
    else:
        # message user and send them to error page
        message.warning(request, 'You can only update you own appointments!')
        return render(request, '403.html')


@login_required
def delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    # making sure if the user owns the appointment before they can update it
    if appointment.user.id != request.user.id:
        # message user and send them to error page
        message.warning(request, 'You can only delete your own appointments!')
        return render(request, '403.html')

    if request.method == 'POST':
        appointment.delete()
        messages.success(request, 'Appointment deleted successfully!')
        return redirect('appointment_list')
    return render(request, 'appointments/appointment_delete.html')


def error_404_view(request, exception):
    """
    Displays 404.html path
    """
    return render(request, '404.html')


def handler500(request, *args, **argv):
    """
    Displays 500.html path
    """
    return render(request, '500.html')


def handler403(request, *args, **argv):
    """
    Displays 403.html path
    """
    return render(request, '403.html')