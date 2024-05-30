from django.contrib import admin
from .models import Region, Comuna, User, Property, Solicitude

# Register your models here.
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(User)   
admin.site.register(Property)   
admin.site.register(Solicitude)

