from django.shortcuts import render, redirect
from main_page.models import UserReservation,TestoMonial
from django.contrib.auth.decorators import login_required, user_passes_test

def is_manager(user):
    return user.groups.filter(name ='managers').exists()



@login_required(login_url='/login/')
@user_passes_test(is_manager)
def reservation_list(request):
    lst = UserReservation.objects.filter(is_processed=False)
    print('lst', lst)
    return render(request, 'reservation_list.html', context={'lst': lst})

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_reservation(request, pk):
    UserReservation.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:manager_view')

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def message_list(request):
    lst1 = TestoMonial.objects.filter(is_answered=False)
    print ('lst1',lst1)
    return render(request, 'message_list.html', context={'lst1': lst1})

@login_required(login_url='/login/')
@user_passes_test(is_manager)
def update_message(request, pk):
    TestoMonial.objects.filter(pk=pk).update(is_answered=True)
    return redirect('manager:message_view')