from django.db import models


# Строжка
class Gouging(models.Model):
    amount_of_material = models.PositiveIntegerField(
        verbose_name='Количество затраченного материала')
    start_date = models.DateTimeField(verbose_name='Дата начала строжки')

    def __str__(self):
        return 'Строжка (№%s) от %s' % (self.id, self.start_date)

    class Meta:
        verbose_name = 'Строжка'
        verbose_name_plural = 'Строжки'


class AdditionalSurfacing(models.Model):
    # Типы труда, с помощью которых осуществляться наплавка.
    type_of_surfacing = models.CharField(max_length=50,
                                         verbose_name='Тип наплавки',
                                         blank=True,
                                         null=True,
                                         default="")
    # Виды расходников, чем осуществляется наплавка.
    type_of_consumables = models.CharField(max_length=50,
                                           verbose_name='Тип расходника',
                                           blank=True,
                                           null=True,
                                           default=""
                                           )
    amount_of_material = models.PositiveIntegerField(
        verbose_name='Количество наплавленного', blank=True, null=True, default="")

    def __str__(self):
        return 'Дополнительная наплавка (№%s)' % self.id

    class Meta:
        verbose_name = 'Дополнительная наплавка'
        verbose_name_plural = 'Дополнительные наплавки'


# Наплавка
class Surfacing(models.Model):
    # TODO: Сделать разделение наплавки на ручную и роботом
    # Типы труда, с помощью которых осуществляться наплавка.
    type_of_surfacing = models.CharField(max_length=50,
                                         verbose_name='Тип наплавки')
    # Виды расходников, чем осуществляется наплавка.
    type_of_consumables = models.CharField(max_length=50,
                                           verbose_name='Тип расходника')
    amount_of_material = models.PositiveIntegerField(
        verbose_name='Количество наплавленного')
    # Дополнительная наплавка
    additional_surfacing = models.ForeignKey(
        AdditionalSurfacing,
        related_name='additional_surfacing',
        on_delete=models.CASCADE,
        verbose_name='Дополнительная наплавка',
        blank=True,
        null=True,
        default=None)
    final_surfacing = models.ForeignKey(AdditionalSurfacing,
                                        related_name='final_surfacing',
                                        on_delete=models.CASCADE,
                                        verbose_name='Окончательная наплавка',
                                        blank=True,
                                        null=True,
                                        default=None)
    start_date = models.DateTimeField(verbose_name='Дата начала наплавки')

    def __str__(self):
        return 'Наплавка (№%s) от %s' % (self.id, self.start_date)

    class Meta:
        verbose_name = 'Наплавка'
        verbose_name_plural = 'Наплавки'


# Т.к. для каждой наплавки надо вести учет затраченного
# материала - создам для этого таблицу для динамической формы,
# свяжу её с родительской таблицей "Наплавка" по внешнему ключу.


# Термообработка
class HeatTreatment(models.Model):
    final_hardness = models.PositiveIntegerField(
        verbose_name='Итоговая твердость')
    start_date = models.DateTimeField(verbose_name='Дата погрузки в печь')

    def __str__(self):
        return 'Теормообработка (№%s) от %s' % (self.id, self.start_date)

    class Meta:
        verbose_name = 'Термообработка'
        verbose_name_plural = 'Термообработки'


# Механообработка
class Machining(models.Model):
    start_date = models.DateTimeField(verbose_name='Дата начала м/о')

    def __str__(self):
        return 'Механообработка (№%s) от %s' % (self.id, self.start_date)

    class Meta:
        verbose_name = 'Механообработка'
        verbose_name_plural = 'Механообработки'


# Главная таблица
class PrimaryTable(models.Model):
    number = models.PositiveIntegerField(verbose_name='Номер оснастки')
    letter = models.CharField(verbose_name='Литера', max_length=50)
    gouging = models.ForeignKey(Gouging,
                                on_delete=models.CASCADE,
                                verbose_name='Строжка',
                                null=True, default=None, blank=True)
    surfacing = models.ForeignKey(Surfacing,
                                  on_delete=models.CASCADE,
                                  verbose_name='Наплавка',
                                  null=True, default=None, blank=True)
    heat_treatment = models.ForeignKey(HeatTreatment,
                                       on_delete=models.CASCADE,
                                       null=True, default=None,
                                       blank=True,
                                       verbose_name='Термообработка')
    machining = models.ForeignKey(Machining,
                                  on_delete=models.CASCADE,
                                  verbose_name='Механообработка',
                                  null=True, default=None, blank=True)
    received_stamp_date = models.DateTimeField(
        verbose_name='Дата поступления штампа')
    customer = models.CharField(verbose_name='Заказчик', max_length=128)
    scheme = models.BooleanField(verbose_name='Чертёж')

    def __str__(self):
        return 'Главная таблица (№%s) для %s' % (self.id, self.customer)

    class Meta:
        verbose_name = 'Главная таблица'
        verbose_name_plural = 'Главные таблицы'
