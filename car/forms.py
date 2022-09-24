from django import forms
from car.models import Car
class carModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'