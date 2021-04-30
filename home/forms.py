from django import forms
from .  models import Booking
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class BookForm(forms.ModelForm):
 
    class Meta : 
        model = Booking
        fields = ("travellers","hotel_name")
        labels = {
            'travellers':'Enter Number Of Travellers ',
            'hotel_name':'Enter Hotel Name',
            
        }

class edituser(UserChangeForm):
    class Meta :
        model = User
        fields= (
            'email',
            'username',
            'first_name',
            'last_name',
        )
