import random
from django.shortcuts import render,redirect
from .models import Category,Dish,Why,Events,About,Chefs,Gallery,Contactus,Contmail,Contphone,UserReservation,\
    TestoMonial,Slides,BestTest
from .forms import UserReservationForm,TestoMonialForm


def main_page(request):
    if request.method == 'POST':
        testomonial = TestoMonialForm(request.POST)
        reservation = UserReservationForm(request.POST)
        if reservation.is_valid():
            reservation.save()
        if testomonial.is_valid():
            testomonial.save()

        return redirect('/')


    reservation = UserReservationForm()
    categories = Category.objects.filter(is_visible=True).order_by('position')
    dishes = Dish.objects.filter(is_visible=True).order_by('position')
    special = Dish.objects.filter(is_visible=True, is_special=True).order_by('position')
    whyus = Why.objects.filter(is_visible=True).order_by('position')[:3]
    events = Events.objects.filter(is_visible=True).order_by('position')
    about = About.objects.filter(is_visible=True)[:1]
    chefs = Chefs.objects.filter(is_visible=True).order_by('position')[:3]
    gallery = Gallery.objects.filter(is_visible=True).order_by('position')
    # gallery = random.sample(sorted(gallery), k=8)
    contact = Contactus.objects.filter(is_visible=True)[:1]
    contmail = Contmail.objects.filter(is_visible=True).order_by('position')
    contphone = Contphone.objects.filter(is_visible=True).order_by('position')
    testomonial = TestoMonialForm()
    slides = Slides.objects.order_by('name')
    besttest = BestTest.objects.order_by('name')

    return render(request,'main.html', context={'categories': categories, 'dishes':dishes,'special':special,
        'whyus':whyus, 'events': events, 'about': about,'chefs': chefs, 'gallery':gallery,
        'contact': contact,'contmail':contmail, 'contphone':contphone,'reservation':reservation,
        'testomonial': testomonial, 'slides':slides, 'besttest': besttest})


