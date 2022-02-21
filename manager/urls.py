from django.urls import path
from .views import reservation_list, update_reservation

app_name = 'manager'

urlpatterns = [
    path('', reservation_list, name='manager_view'),
    path('reservations/update/<int:pk>/',update_reservation,name ='update_res')
]
