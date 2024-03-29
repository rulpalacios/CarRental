# Generated by Django 2.2.2 on 2019-06-24 02:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=250)),
                ('car_type', models.CharField(choices=[('hybrid', 'HYBRID'), ('diesel', 'DIESEL'), ('gasoline', 'GASOLINE'), ('electric', 'ELECTRIC')], default='gasoline', max_length=8)),
                ('cost', models.CharField(max_length=10)),
                ('image', models.CharField(max_length=35)),
                ('transmission', models.CharField(choices=[('automatic', 'Automatic'), ('manual', 'Manual')], default='manual', max_length=9)),
                ('seats', models.IntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_cars', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
