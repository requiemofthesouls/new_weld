from django import forms
import datetime
from .models import *


# Строжка
class GougingForm(forms.ModelForm):
    amount_of_material = forms.IntegerField(min_value=0, help_text='Количество затраченного материала')
    spent_time = forms.IntegerField(min_value=0, help_text='Затраченное время (ч)')
    start_date = forms.DateTimeField(widget=forms.TextInput(
        attrs={
            'id': 'example'
        }), help_text='Дата начала строжки', initial=datetime.date.today)

    class Meta:
        model = Gouging
        fields = ('amount_of_material', 'spent_time', 'start_date')


# Наплавка
class SurfacingForm(forms.ModelForm):
    amount_of_material = forms.IntegerField(min_value=0, help_text='Количество наплавленного')
    type_of_consumables = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=CONSUMABLES)
    spent_time = forms.IntegerField(min_value=0, help_text='Время работы робота (ч)')
    start_date = forms.DateTimeField(widget=forms.TextInput(
        attrs={
            'id': 'example'
        }), help_text='Дата начала наплавки')

    class Meta:
        model = Surfacing
        fields = ('amount_of_material', 'spent_time', 'type_of_consumables', 'start_date')


# Термообработка
class HeatTreatmentForm(forms.ModelForm):
    time_in_oven = forms.IntegerField(min_value=0, help_text='Время в печи (ч)')
    final_hardness = forms.IntegerField(min_value=0, help_text='Итоговая твердость')
    start_date = forms.DateTimeField(widget=forms.TextInput(
        attrs={
            'id': 'example'
        }), help_text='Дата начала термообработки')

    class Meta:
        model = HeatTreatment
        fields = ('time_in_oven', 'final_hardness', 'start_date')


# Механообработка
class MachiningForm(forms.ModelForm):
    start_date = forms.DateTimeField(widget=forms.TextInput(
        attrs={
            'id': 'example'
        }), help_text='Дата начала термообработки')
    machine_time = forms.IntegerField(min_value=0, help_text='Время работы станка (ч)')

    class Meta:
        model = HeatTreatment
        fields = ('start_date', 'machine_time')


# Главная таблица
class PrimaryTableForm(forms.ModelForm):
    number = forms.IntegerField(help_text='Номер оснастки', label="Номер оснастки")
    letter = forms.CharField(help_text='Литера', label='Литера')
    gouging = forms.ModelChoiceField(queryset=Gouging.objects.all(),
                                     help_text='Строжка', label='Строжка')
    surfacing = forms.ModelChoiceField(queryset=Surfacing.objects.all(),
                                       help_text='Наплавка', label='Наплавка')
    heat_treatment = forms.ModelChoiceField(queryset=HeatTreatment.objects.all(),
                                            help_text='Термообработка', label='Термообработка')
    machining = forms.ModelChoiceField(queryset=Machining.objects.all(),
                                       help_text='Механообработка', label='Механообработка')
    received_stamp_date = forms.DateTimeField(widget=forms.TextInput(
        attrs={
            'id': 'example'
        }),
        help_text='Дата поступления штампа',
        initial=datetime.date.today,
        label='Дата поступления штампа')
    customer = forms.CharField(help_text='Заказчик', label='Заказчик')
    scheme = forms.BooleanField(help_text='Чертёж', label='Чертёж')

    class Meta:
        model = PrimaryTable
        fields = ('number', 'letter', 'gouging', 'surfacing', 'heat_treatment',
                  'machining', 'received_stamp_date', 'customer', 'scheme')
