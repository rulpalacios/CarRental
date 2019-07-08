from django.urls import path
from . import views

app_name = 'car_rental'

urlpatterns = [
    #car views
    path('cars', views.index),
    path('new', views.new),
    path('show/<str:slug>', views.show),
    path('delete/<str:slug>', views.delete),
    path('edit/<str:slug>',views.edit)
]
