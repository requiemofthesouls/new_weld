from django import forms
import datetime
from .models import *
from tempus_dominus.widgets import DateTimePicker, DatePicker, TimePicker


# Строжка
class GougingForm(forms.ModelForm):
    amount_of_material = forms.IntegerField(min_value=0, help_text='Количество затраченного материала')
    spent_time = forms.TimeField(help_text='Затраченное время (ч)')
    start_date = forms.CharField(widget=forms.TextInput(
        attrs={
            'id': 'example'
        }))

    class Meta:
        model = Gouging
        fields = ('amount_of_material', 'spent_time', 'start_date')
