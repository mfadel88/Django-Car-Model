from django.db import models
from django.shortcuts import reverse
# from django.urls import reverse


# Create your models here.
class Car(models.Model):
    model = models.CharField(max_length=100)
    production = models.CharField(max_length=1000)
    price = models.IntegerField(default=0)


    def __str__(self):
        return f"{self.model}"


    def get_all_car(cls):
        return cls.object.all()

    def get_show_url(self):
        return reverse("car.show", args=[self.id])

    def get_edit_url(self):
        return reverse("car.edit", args=[self.id])

    def get_delete_url(self):
        return reverse("car.delete", args=[self.id])