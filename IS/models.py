from django.db import models


#Типы расходников
CONSUMABLES = (
    ('Ф', 'Ф'),
    ('М', 'М')
    )


# Строжка
class Gouging(models.Model):
    amount_of_material = models.PositiveIntegerField(
        verbose_name='Количество затраченного материала')
    spent_time = models.TimeField(verbose_name='Затраченное время')
    start_date = models.DateTimeField(verbose_name='Дата начала строжки')

    def __str__(self):
        return 'Строжка (%s) %s' % (self.id, self.start_date)

    class Meta:
        verbose_name = 'Строжка'
        verbose_name_plural = 'Строжки'


# Наплавка
class Surfacing(models.Model):
    amount_of_material = models.PositiveIntegerField(
        verbose_name='Количество наплавленного')
    type_of_consumables = models.CharField(choices=CONSUMABLES,
                                           max_length=50,
                                           verbose_name='Тип расходника')
    robot_work_time = models.TimeField(verbose_name='Время работы робота')
    start_date = models.DateTimeField(verbose_name='Дата начала наплавки')

    def __str__(self):
        return 'Наплавка (%s) %s' % (self.id, self.start_date)

    class Meta:
        verbose_name = 'Наплавка'
        verbose_name_plural = 'Наплавки'


# Термообработка
class HeatTreatment(models.Model):
    time_in_oven = models.TimeField(verbose_name='Время в печи')
    final_hardness = models.PositiveIntegerField(verbose_name='Итоговая твердость')
    start_date = models.DateTimeField(verbose_name='Дата погрузки в печь')

    def __str__(self):
        return 'Теормообработка (%s) %s' % (self.id, self.start_date)

    class Meta:
        verbose_name = 'Термообработка'
        verbose_name_plural = 'Термообработки'


# Механообработка
class Machining(models.Model):
    start_date = models.DateTimeField(verbose_name='Дата начала работы')
    machine_time = models.TimeField(verbose_name='Время работы станка')

    def __str__(self):
        return 'Механообработка (%s) %s' % (self.id, self.start_date)

    class Meta:
        verbose_name = 'Механообработка'
        verbose_name_plural = 'Механообработки'


# Главная таблица
class PrimaryTable(models.Model):
    number = models.PositiveIntegerField(verbose_name='Номер оснастки')
    letter = models.CharField(max_length=1,
                              verbose_name='Литера')
    gouging = models.ForeignKey(Gouging,
                                on_delete=models.CASCADE,
                                verbose_name='Строжка')
    surfacing = models.ForeignKey(Surfacing,
                                  on_delete=models.CASCADE,
                                  verbose_name='Наплавка')
    first_heat_treatment = models.ForeignKey(HeatTreatment,
                                             on_delete=models.CASCADE,
                                             related_name='first_heat_treatment',
                                             verbose_name='Первичная термообработка')
    second_heat_treatment = models.ForeignKey(HeatTreatment,
                                              on_delete=models.CASCADE,
                                              related_name='second_heat_treatment',
                                              verbose_name='Вторичная термообработка')
    machining = models.ForeignKey(Machining,
                                  on_delete=models.CASCADE,
                                  verbose_name='Механообработка')
    received_stamp_date = models.DateTimeField(verbose_name='Дата поступления штампа')
    customer = models.CharField(verbose_name='Заказчик', max_length=128)
    scheme = models.BooleanField(verbose_name='Чертёж')

    def __str__(self):
        return 'Главная таблица (%s) %s' % (self.id, self.customer)

    class Meta:
        verbose_name = 'Главная таблица'
        verbose_name_plural = 'Главные таблицы'
