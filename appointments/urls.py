from django.urls import path
from .views import appointments, homepage


urlpatterns = [
    path('', homepage.HomePageView.as_view(), name='home'),
    path('list/', appointments.list, name='appointment_list'),
    path('appointments/<int:pk>/', appointments.detail, name='appointment_detail'),  # noqa
    path('create/', appointments.create, name='appointment_create'),
    path('update/<int:pk>', appointments.update, name='appointment_update'),
    path('delete/<int:pk>', appointments.delete, name='appointment_delete'),
    path('403', appointments.Page403.as_view(), name='403'),
    path('404', appointments.Page404.as_view(), name='404'),
    path('500', appointments.Page500.as_view(), name='500'),
]

