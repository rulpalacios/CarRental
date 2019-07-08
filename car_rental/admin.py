from django.contrib import admin
from .models import Car

# Register your models here.
@admin.register(Car)

class CarAdmin(admin.ModelAdmin):
    list_display = ('name','slug','car_type','cost','transmission',
                    'seats','owner')
    search_fields = ('name','cost','transmission','seats')
    list_filter = ('transmission','car_type')