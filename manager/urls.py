from django.urls import path
from .views import reservation_list, update_reservation, message_list,update_message

app_name = 'manager'

urlpatterns = [

    path('', message_list, name='message_view'),
    path('testomonial/update/<int:pk>/', update_message, name='update_mes'),
    path('', reservation_list, name='manager_view'),
    path('reservations/update/<int:pk>/',update_reservation,name ='update_res'),
]
