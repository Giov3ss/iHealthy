from django.urls import path
from .views import appointments, homepage


urlpatterns = [
    path('', homepage.HomePageView.as_view(), name='home'),
    path('list/', appointments.list, name='appointment_list'),
    path('appointments/<int:pk>/', appointments.detail, name='appointment_detail'),  # noqa
    path('create/', appointments.create, name='appointment_create'),
    path('update/<int:pk>', appointments.update, name='appointment_update'),
    path('delete/<int:pk>', appointments.delete, name='appointment_delete'),
]
