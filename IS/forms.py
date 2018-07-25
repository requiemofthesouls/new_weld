from datetime import datetime

from django import forms

from .models import (Gouging, Surfacing, HeatTreatment,
                     Machining, PrimaryTable)


# Строжка
class GougingForm(forms.ModelForm):
    amount_of_material = forms.IntegerField(min_value=0, help_text='Количество затраченного материала',
                                            label='Количество затраченного материала')
    # spent_time = forms.IntegerField(min_value=0, help_text='Затраченное время (ч)',
    #                                 label='Затраченное время (ч)')
    start_date = forms.DateTimeField(widget=forms.TextInput(
        attrs={
            'id': 'gouging_pickdatetime',
            'readonly': 'true',
        }),
        help_text='Дата начала строжки',
        initial=datetime.now().strftime("%d.%m.%Y %H:%M"),
        label='Дата начала строжки')

    class Meta:
        model = Gouging
        fields = ('amount_of_material', 'start_date')


# Наплавка
class SurfacingForm(forms.ModelForm):
    amount_of_material = forms.IntegerField(min_value=0, help_text='Количество наплавленного',
                                            label='Количество наплавленного')
    # Типы расходников
    CONSUMABLES = (
        ('Ф', 'Проволока 1'),
        ('D', 'Проволока 2'),
        ('B', 'Проволока 3'),
        ('C', 'Проволока 4'),
        ('М', 'Проволока 5')
    )
    type_of_consumables = forms.ChoiceField(choices=CONSUMABLES, label='Тип расходника')
    # robot_work_time = forms.IntegerField(min_value=0, help_text='Время работы робота (ч)',
    #                                      label='Время работы робота (ч)')
    start_date = forms.DateTimeField(widget=forms.TextInput(
        attrs={
            'id': 'surfacing_pickdatetime',
            'readonly': 'true',
        }),
        help_text='Дата начала наплавки',
        initial=datetime.now().strftime("%d.%m.%Y %H:%M"),
        label='Дата начала наплавки')

    class Meta:
        model = Surfacing
        fields = ('amount_of_material', 'type_of_consumables', 'start_date')


# Термообработка
class HeatTreatmentForm(forms.ModelForm):
    # time_in_oven = forms.IntegerField(min_value=0, help_text='Время в печи (ч)',
    #                                   label='Время в печи (ч)')
    final_hardness = forms.IntegerField(min_value=0, help_text='Итоговая твердость',
                                        label='Итоговая твердость')
    start_date = forms.DateTimeField(widget=forms.TextInput(
        attrs={
            'id': 'heat_treatment_pickdatetime',
            'readonly': 'true',
        }),
        help_text='Дата начала термообработки',
        initial=datetime.now().strftime("%d.%m.%Y %H:%M"),
        label='Дата начала термообработки')

    class Meta:
        model = HeatTreatment
        fields = ('final_hardness', 'start_date')


# Механообработка
class MachiningForm(forms.ModelForm):
    start_date = forms.DateTimeField(widget=forms.TextInput(
        attrs={
            'id': 'machining_pickdatetime',
            'readonly': 'true',
        }),
        help_text='Время механообработки',
        initial=datetime.now().strftime("%d.%m.%Y %H:%M"),
        label='Время начала м/о')

    # machine_time = forms.IntegerField(min_value=0, help_text='Время работы станка (ч)',
    #                                   label='Время работы станка (ч)')

    class Meta:
        model = Machining
        fields = ('start_date',)


# Главная таблица
class PrimaryTableForm(forms.ModelForm):
    number = forms.IntegerField(min_value=0, help_text='Номер оснастки', label="Номер оснастки")
    letter = forms.CharField(help_text='Литера', label='Литера')
    received_stamp_date = forms.DateTimeField(widget=forms.TextInput(
        attrs={
            'id': 'pt_pickdatetime',
            'readonly': 'true',
        }),
        help_text='Дата поступления штампа',
        initial=datetime.now().strftime("%d.%m.%Y %H:%M"),
        label='Дата поступления штампа')
    customer = forms.CharField(help_text='Заказчик', label='Заказчик')
    scheme = forms.BooleanField(help_text='Чертёж', label='Чертёж', required=False, initial=False)

    class Meta:
        model = PrimaryTable
        fields = ('number', 'letter', 'received_stamp_date', 'customer', 'scheme')
