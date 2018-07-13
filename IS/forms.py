from django import forms
import datetime
from .models import *


# Строжка
class GougingForm(forms.ModelForm):
    amount_of_material = forms.IntegerField(min_value=0, help_text='Количество затраченного материала',
                                            label='Количество затраченного материала')
    spent_time = forms.IntegerField(min_value=0, help_text='Затраченное время (ч)',
                                    label='Затраченное время (ч)')
    start_date = forms.DateTimeField(widget=forms.TextInput(
        attrs={
            'id': 'pickdatetime'
        }),
        help_text='Дата начала строжки',
        initial=datetime.date.today,
        label='Дата начала строжки')

    class Meta:
        model = Gouging
        fields = '__all__'


# Наплавка
class SurfacingForm(forms.ModelForm):
    amount_of_material = forms.IntegerField(min_value=0, help_text='Количество наплавленного',
                                            label='Количество наплавленного')
    type_of_consumables = forms.ChoiceField(choices=CONSUMABLES, label='Тип расходника')
    robot_work_time = forms.IntegerField(min_value=0, help_text='Время работы робота (ч)',
                                         label='Время работы робота (ч)')
    start_date = forms.DateTimeField(widget=forms.TextInput(
        attrs={
            'id': 'pickdatetime'
        }),
        help_text='Дата начала наплавки',
        label='Дата начала наплавки')

    class Meta:
        model = Surfacing
        fields = '__all__'


# Термообработка
class HeatTreatmentForm(forms.ModelForm):
    time_in_oven = forms.IntegerField(min_value=0, help_text='Время в печи (ч)',
                                      label='Время в печи (ч)')
    final_hardness = forms.IntegerField(min_value=0, help_text='Итоговая твердость',
                                        label='Итоговая твердость')
    start_date = forms.DateTimeField(widget=forms.TextInput(
        attrs={
            'id': 'pickdatetime'
        }),
        help_text='Дата начала термообработки',
        label='Дата начала термообработки')

    class Meta:
        model = HeatTreatment
        fields = '__all__'


# Механообработка
class MachiningForm(forms.ModelForm):
    start_date = forms.DateTimeField(widget=forms.TextInput(
        attrs={
            'id': 'pickdatetime'
        }),
        help_text='Дата начала механообработки',
        label='Дата начала механообработки')
    machine_time = forms.IntegerField(min_value=0, help_text='Время работы станка (ч)',
                                      label='Время работы станка (ч)')

    class Meta:
        model = Machining
        fields = '__all__'


# Главная таблица
class PrimaryTableForm(forms.ModelForm):
    number = forms.IntegerField(help_text='Номер оснастки', label="Номер оснастки")
    letter = forms.CharField(help_text='Литера', label='Литера')
    received_stamp_date = forms.DateTimeField(widget=forms.TextInput(
        attrs={
            'id': 'pickdatetime'
        }),
        help_text='Дата поступления штампа',
        initial=datetime.date.today,
        label='Дата поступления штампа')
    customer = forms.CharField(help_text='Заказчик', label='Заказчик')
    scheme = forms.BooleanField(help_text='Чертёж', label='Чертёж', required=False)

    class Meta:
        model = PrimaryTable
        fields = ('number', 'letter', 'received_stamp_date', 'customer', 'scheme')
