from django.contrib import admin
from hotel.models import Place,Offers,Rooms,Hotel

# Register your models here.

admin.site.register(Place)
admin.site.register(Hotel)
admin.site.register(Rooms)
admin.site.register(Offers)
