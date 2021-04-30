from django.contrib import admin

# Register your models here.
from .models import Booking, Contact, Hotels, Image
admin.site.register(Contact)
admin.site.register(Image)
admin.site.register(Booking)
admin.site.register(Hotels)