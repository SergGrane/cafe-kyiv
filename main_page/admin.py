from django.contrib import admin
from .models import Category,Dish,Why,Events,About,Chefs,Gallery,Contactus,Contmail,Contphone,UserReservation,\
    TestoMonial, Slides, BestTest

#admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'is_visible','position']
    list_filter = ['name']


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'desc','is_visible', 'position','photo']
    list_filter = ['name','category']

@admin.register(Why)
class WhyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc', 'is_visible', 'position']
    list_filter = ['name','position']


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'head', 'row1','row2','row3', 'bottom','photo','is_visible', 'position']
    list_filter = ['name','price','position']

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'head1','head2', 'head3', 'row1','row2','row3', 'bottom','about_video', 'is_visible']
    list_filter = ['name']

@admin.register(Chefs)
class ChefsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'speciality', 'photo', 'twit', 'faceb', 'insta', 'linked', 'position','is_visible']
    list_filter = ['name','speciality']

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'position','is_visible']
    list_filter = ['position']

@admin.register(Contactus)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'map', 'street', 'city', 'opendays','openhours', 'position','is_visible']
    list_filter = ['position']


@admin.register(Contmail)
class ContmailAdmin(admin.ModelAdmin):
    list_display = ['id', 'mail', 'position', 'is_visible']
    list_filter = ['position']


@admin.register(Contphone)
class ContphoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'position', 'is_visible']
    list_filter = ['position']

admin.site.register(UserReservation)

@admin.register(TestoMonial)
class TestAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'mail', 'subj','message', 'date', 'is_answered']
    list_filter = ['name','date','subj']

@admin.register(Slides)
class SlideAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'rows']
    list_filter = ['name']

@admin.register(BestTest)
class BestTestAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'profession','message',  'is_visible']
    list_filter = ['name','profession']


