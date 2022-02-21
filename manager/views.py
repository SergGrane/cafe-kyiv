from django.shortcuts import render, redirect
from main_page.models import UserReservation
from django.contrib.auth.decorators import login_required, user_passes_test

def is_manager(user):
    return user.groups.filter(name ='managers').exists()



@login_required(login_url='/login/')
@user_passes_test(is_manager)
def reservation_list(request):
    lst = UserReservation.objects.filter(is_processed=False)

    return render(request, 'reservation_list.html', context={'lst': lst})

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_reservation(request, pk):
    UserReservation.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:manager_view')


