from django.shortcuts import render
from car.forms import carModelForm
# Create your views here.
# import car.models
from car.models import Car
from django.views.generic import  DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def carIndex(request):
    allcar = Car.get_all_car()
    return render(request, "car/index.html", context={"car": allcar})


class CarDetails(DetailView):
    model = Car
    template_name = "car/show.html"


class CreateCarView(CreateView):
    template_name = "car/create.html"
    form_class = carModelForm
    success_url = '/car/index'

class EditCarView(UpdateView):
    template_name = "car/edit.html"
    form_class = carModelForm
    success_url = '/car/index'
    model = Car



class DeleteCarView(DeleteView):
    template_name = "car/delete.html"
    model = Car
    success_url = '/car/index'
