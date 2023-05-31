from django.shortcuts import render, get_object_or_404, redirect
from ..models import Appointment
from ..forms import AppointmentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.base import TemplateView


@login_required
def list(request):
    """
    View List appointments for the logged-in user.

    1. Retrieve all appointments associated with the logged-in user.
    2. Render the list.html template, passing the appointments as context variable.  # noqa

    """
    appointments = Appointment.objects.filter(user_id=request.user.id)
    return render(request, 'appointments/list.html', {'appointments': appointments})  # noqa


@login_required
def detail(request, pk):
    """
    View to display the details of a specific appointment.

    1. Get the appointment based on the provided primary key (pk).
    2. Render the detail.html template, passing the appointment as a context variable.  # noqa

    """
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, 'appointments/detail.html', {'appointment': appointment})  # noqa


@login_required
def create(request):
    """
    View to create a new appointment.

    1. Create a form for creating an appointment, passing the user ID and form data.  # noqa
    2. if the form is valid, save the new appointment, display a success messeage and redirect to te appointment list.  # noqa
    3. Render the form.html template for creating an appointment.

    """
    form = AppointmentForm(request.user.id, request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'You have created an appointment!')
        return redirect('appointment_list')
    return render(request, 'appointments/form.html', {'form': form, 'title': 'Create'})  # noqa


@login_required
def update(request, pk):
    """
    View to update an appointment.

    1. Get the appointment based on the provided primary key (pk).
    2. Create a form for updating the appointment, passing the user ID, 
    form data and instance (exiting appointment.)
    3. If the user owns the appointment:
        - If the form is valid, save the update appointment and display a success message.  # noqa
        - Render the form.html template for updating the appointment.
    4. If the user does not own the appointment:
        - Display a warning message indicating unauthorized access and render the 403.html template.  # noqa

    """
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
    """
    View to delete an appointment.

    1. Get the appointment based on the provided primary key (pk).
    2. Check if the user owns the appointment.
        - If not, display a warning message indicating unauthorized access and render the 403.html template.  # noqa
    3. If the request method is POST, delete the appointment, display a success message and redirect to the appointment list.  # noqa
    4. Render the appointment_delete.html template for confirming the appointment deletion.  # noqa

    """
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
    return render(request, '404.html', status=404)


def handler500(request, *args, **argv):
    """
    Displays 500.html path
    """
    return render(request, '500.html', status=500)


def handler403(request, *args, **argv):
    """
    Displays 403.html path
    """
    return render(request, '403.html', status=403)
