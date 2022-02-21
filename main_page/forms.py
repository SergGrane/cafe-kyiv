from django import forms
from .models import UserReservation,TestoMonial

class TestoMonialForm(forms.ModelForm):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={
                               'type': "text",
                               'name': "name",
                               'class': "form-control",
                               'id': "name",
                               'placeholder': "Your Name",

                           }))
    mail = forms.EmailField(widget=forms.EmailInput(attrs={
        'type' : "email",
        'class' :"form-control",
        'name' : "email",
        'id' : "email",
        'placeholder' : "Your Email"

    }))

    subj = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={
                               'type' : "text",
                               'class' :"form-control",
                               'name' : "subj",
                               'id' : "subject",
                               'placeholder' : "Subject"}))

    message = forms.CharField(max_length=500,widget=forms.TextInput(attrs={
    'class' :"form-control",
    'name' : "message",
    'rows' : "5",
    'placeholder' : "Message"


    }))
    class Meta:
        model = TestoMonial
        fields = ('name', 'mail', 'subj', 'message')




class UserReservationForm(forms.ModelForm):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={
                               'type': "text",
                               'name': "name",
                               'class': "form-control",
                               'id': "name",
                               'placeholder': "Your Name",
                               'data-rule': "minlen:4",
                               'data-msg': "Please enter at least 4 chars"
                           }))
    phone = forms.CharField(max_length=15,
                            widget=forms.TextInput(
                                attrs={'type': 'text', 'name': 'phone', 'id': 'phone', 'class': 'form-control',
                                       'placeholder': 'Телефон', 'required': 'required',
                                       'data-rule': 'minlen:4', 'data-msg': 'Please enter at least 4 chars'}))
    persons = forms.IntegerField(widget=forms.NumberInput(attrs={
        'type': "number",
        'class': "form-control",
        'name': "people",
        'id': "people",
        'placeholder': "# of people",
        'data-rule': "minlen:1",
        'data-msg': "Please enter at least 1 chars"}))

    message = forms.CharField(max_length=400,
                              widget=forms.Textarea(
                                  attrs={'type': 'message', 'name': 'message', 'class': 'form-control',
                                         'rows': '5', 'placeholder': 'Сообщение', 'required': 'required'}))


    class Meta:
        model = UserReservation
        fields = ('name', 'phone', 'persons', 'message')
