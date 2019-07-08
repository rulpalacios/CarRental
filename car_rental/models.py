from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Car(models.Model):
    TRANSMISSION_CHOICES = (
        ('automatic', 'Automatic'),
        ('manual', 'Manual')
    )
    TYPES_CHOICES = (
        ('hybrid','HYBRID'),
        ('diesel', 'DIESEL'),
        ('gasoline', 'GASOLINE'),
        ('electric','ELECTRIC'),
    )
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=250)
    car_type = models.CharField(
        max_length=8,
        choices=TYPES_CHOICES,
        default='gasoline'
    )
    cost = models.CharField(max_length=10)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    transmission = models.CharField(
        max_length=9,
        choices=TRANSMISSION_CHOICES,
        default='manual'
    )
    seats = models.IntegerField()
    owner = models.ForeignKey(User,
        on_delete=models.CASCADE,
        related_name='my_cars'
    )

