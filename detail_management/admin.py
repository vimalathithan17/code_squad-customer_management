from django.contrib import admin
from .models import Customer,CustomerProfile,TravelHistory
# Register your models here.
admin.site.register(Customer)
admin.site.register(CustomerProfile)
admin.site.register(TravelHistory)