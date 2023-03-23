from django.urls import path
from .views import appointments

urlpatterns = [
    path('', appointments.list, name='home'),
    path('list/', appointments.list, name='appointment_list'),
    path('create/', appointments.create, name='appointment_create')
]