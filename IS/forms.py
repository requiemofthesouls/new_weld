from django import forms
import datetime
from .models import *


# Строжка
class GougingForm(forms.ModelForm):
    amount_of_material = forms.IntegerField(min_value=0, help_text='Количество затраченного материала')
    spent_time = forms.TimeField(help_text='Затраченное время (ч)')
    start_date = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'example'
        }), help_text='Дата начала строжки')

    class Meta:
        model = Gouging
        fields = ('amount_of_material', 'spent_time', 'start_date')


# Наплавка
class SurfacingForm(forms.ModelForm):
    amount_of_material = forms.IntegerField(min_value=0, help_text='Количество наплавленного')
    type_of_consumables = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=CONSUMABLES)
    spent_time = forms.TimeField(help_text='Время работы робота (ч)')
    start_date = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'example'
        }), help_text='Дата начала наплавки')

    class Meta:
        model = Surfacing
        fields = ('amount_of_material', 'spent_time', 'type_of_consumables', 'start_date')
