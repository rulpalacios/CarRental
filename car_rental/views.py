from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Car
from car_rental.forms import CarForm  

# Create your views here.

def index(request):
    # cars = Car.objects.all()
    # return render(request, 
    #             'rental/car/list.html',
    #             {'cars': cars} )
    cars = Car.objects.all()
    paginator = Paginator(cars, 6) # 6 cars in each page
    
    page = request.GET.get('page')
    cars = paginator.get_page(page)
    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        # If page isnt an integer deliver the first page
        cars = paginator.page(1)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)

    return render(request, 
                'rental/car/list.html',
                {'cars': cars} )

def new(request):
    if request.method == 'POST':
        form = CarForm(request.POST or None, 
                        request.FILES or None) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Auto credo correctamente')
            return redirect('/rental/cars')
        else:
            return render(request,
            'rental/car/new.html',
            {'form':form})
    else:
        form = CarForm() 
        return render(request,
            'rental/car/new.html',
            {'form':form})

def show(request, slug):
    car = Car.objects.get(slug = slug)
    return render(request,
                'rental/car/show.html',
                {'car': car})

def edit(request,slug):
    car = Car.objects.get(slug = slug)
    return render(request,
                'rental/car/edit.html',
                {'car': car})

def delete(request, slug):
    car = Car.objects.get(slug = slug)
    car.delete()
    messages.success(request, 'Auto eliminado correctamente')
    return redirect('/rental/cars')