from django.urls import path
from .views import appointments

urlpatterns = [
    path('', appointments.list, name='home'),
    path('list/', appointments.list, name='appointment_list'),
]