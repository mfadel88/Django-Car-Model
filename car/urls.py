
from django.urls import path
from car.views import carIndex, CarDetails, CreateCarView, EditCarView, DeleteCarView
urlpatterns = [
    path('index',carIndex),
    path('details/<int:pk>', CarDetails.as_view(), name='car.show'),
    path('create',CreateCarView.as_view()),
    path('edit/<int:pk>',EditCarView.as_view(), name='car.edit'),
    path('delete/<int:pk>',DeleteCarView.as_view(), name='car.delete'),
]
