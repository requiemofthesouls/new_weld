from datetime import datetime

from django import forms

from .models import (Gouging,
                     HeatTreatment,
                     AdditionalSurfacing,
                     Machining,
                     PrimaryTable,
                     Surfacing)


# Строжка
class GougingForm(forms.ModelForm):
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


# Дополнительная наплавка
class AdditionalSurfacingForm(forms.ModelForm):
    # Типы труда, с помощью которых осуществляться наплавка.
    TYPES_OF_WORK = (
        ('Manual', 'Ручная'),
        ('Robot', 'Робот')
    )
    type_of_surfacing = forms.ChoiceField(choices=TYPES_OF_WORK,
                                          label='Тип наплавки',
                                          initial='Manual', required=False)
    # Типы расходников
    CONSUMABLES = (
        ('Ф', 'Проволока 1'),
        ('D', 'Проволока 2'),
        ('B', 'Проволока 3'),
        ('C', 'Проволока 4'),
        ('М', 'Проволока 5')
    )
    type_of_consumables = forms.ChoiceField(
        choices=CONSUMABLES,
        label='Тип расходника',
        initial='D',
        required=False)
    amount_of_material = forms.IntegerField(
        min_value=0,
        help_text='Количество наплавленного',
        label='Количество наплавленного',
        initial='',
        required=False)

    class Meta:
        model = AdditionalSurfacing
        fields = ('type_of_surfacing',
                  'type_of_consumables',
                  'amount_of_material',)


# Окончательная наплавка
class FinalSurfacingForm(forms.ModelForm):
    # Типы труда, с помощью которых осуществляться наплавка.
    TYPES_OF_WORK = (
        ('Manual', 'Ручная'),
        ('Robot', 'Робот')
    )
    type_of_surfacing = forms.ChoiceField(choices=TYPES_OF_WORK,
                                          label='Тип наплавки',
                                          initial='Manual', required=False)
    # Типы расходников
    CONSUMABLES = (
        ('Ф', 'Проволока 1'),
        ('D', 'Проволока 2'),
        ('B', 'Проволока 3'),
        ('C', 'Проволока 4'),
        ('М', 'Проволока 5')
    )
    type_of_consumables = forms.ChoiceField(
        choices=CONSUMABLES,
        label='Тип расходника',
        initial='D',
        required=False)
    amount_of_material = forms.IntegerField(
        min_value=0,
        help_text='Количество наплавленного',
        label='Количество наплавленного',
        initial='',
        required=False)

    class Meta:
        model = AdditionalSurfacing
        fields = ('type_of_surfacing',
                  'type_of_consumables',
                  'amount_of_material',)


class MaterialForm(forms.Form):
    """
    Форма учета расхода материалов
    """
    # Типы расходников
    CONSUMABLES = (
        ('Ф', 'Проволока 1'),
        ('D', 'Проволока 2'),
        ('B', 'Проволока 3'),
        ('C', 'Проволока 4'),
        ('М', 'Проволока 5')
    )
    type_of_consumables = forms.ChoiceField(
        choices=CONSUMABLES,
        label='Тип расходника',
        initial='',
        required=False)
    amount_of_material = forms.IntegerField(
        min_value=0,
        help_text='Количество наплавленного',
        label='Количество наплавленного',
        initial='',
        required=False)


# Наплавка
class SurfacingForm(forms.ModelForm):
    # Типы труда, с помощью которых осуществляться наплавка.
    TYPES_OF_WORK = (
        ('Manual', 'Ручная'),
        ('Robot', 'Робот')
    )
    type_of_surfacing = forms.ChoiceField(choices=TYPES_OF_WORK,
                                          label='Тип наплавки',
                                          initial='Robot')

    # Типы расходников
    CONSUMABLES = (
        ('Ф', 'Проволока 1'),
        ('D', 'Проволока 2'),
        ('B', 'Проволока 3'),
        ('C', 'Проволока 4'),
        ('М', 'Проволока 5')
    )
    type_of_consumables = forms.ChoiceField(
        choices=CONSUMABLES, label='Тип расходника')

    amount_of_material = forms.IntegerField(
        min_value=0,
        help_text='Количество наплавленного',
        label='Количество наплавленного')
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
        fields = ('type_of_surfacing',
                  'type_of_consumables',
                  'amount_of_material',
                  'start_date')


# Термообработка
class HeatTreatmentForm(forms.ModelForm):
    final_hardness = forms.IntegerField(
        min_value=0,
        help_text='Итоговая твердость',
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

    class Meta:
        model = Machining
        fields = ('start_date',)


# Главная таблица
class PrimaryTableForm(forms.ModelForm):
    number = forms.IntegerField(
        min_value=0,
        help_text='Номер оснастки',
        label="Номер оснастки")
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
    scheme = forms.BooleanField(
        help_text='Чертёж',
        label='Чертёж',
        required=False,
        initial=False)

    class Meta:
        model = PrimaryTable
        fields = (
            'number',
            'letter',
            'received_stamp_date',
            'customer',
            'scheme')
