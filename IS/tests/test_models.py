from datetime import datetime, timedelta

from django.test import TestCase

from IS.models import PrimaryTable, Gouging, \
    Surfacing, HeatTreatment, Machining


class PrimaryTableModelTest(TestCase):
    """Тестирование модели главной таблицы (оснастки)."""

    @classmethod
    def setUpTestData(cls):
        # Создаём связанные объекты
        Gouging.objects.create(amount_of_material=2, spent_time=4,
                               start_date=datetime.now() + timedelta(hours=2))
        Surfacing.objects.create(amount_of_material=6, type_of_consumables='D',
                                 robot_work_time=3,
                                 start_date=datetime.now() + timedelta(hours=4))
        HeatTreatment.objects.create(time_in_oven=14, final_hardness=402,
                                     start_date=datetime.now() + timedelta(hours=6))
        Machining.objects.create(start_date=datetime.now() + timedelta(hours=8),
                                 machine_time=20)

        # Создаём объект оснастки который будем использовать в тестах,
        # но не будем изменять
        PrimaryTable.objects.create(number='1234567890', letter='GH01E200',
                                    gouging_id=1, surfacing_id=1,
                                    heat_treatment_id=1, machining_id=1,
                                    received_stamp_date=datetime.now(),
                                    customer='Паша Техник', scheme=True)

    def test_primary_table_label(self):
        """ Сверяет str метод оснастки (primary table) """
        print("Method: test_primary_table_label")
        primary_table = PrimaryTable.objects.get(id=1)
        primary_table_label = primary_table.__str__()
        self.assertEquals(primary_table_label, 'Главная таблица (№1) для Паша Техник')
        print('Result:', primary_table_label)

    def test_dates(self):
        """ Проверяет достоверность дат.
        Делается ли весь техпроцесс после поступления штампа. """
        print('Method: Dates test')
        primary_table = PrimaryTable.objects.get(id=1)
        gouging = Gouging.objects.get(id=1)
        surfacing = Surfacing.objects.get(id=1)
        heat_treatment = HeatTreatment.objects.get(id=1)
        machining = Machining.objects.get(id=1)
        primary_table_date = primary_table.received_stamp_date
        gouging_date = gouging.start_date
        surfacing_date = surfacing.start_date
        heat_treatment_date = heat_treatment.start_date
        machining_date = machining.start_date
        self.assertTrue(True if primary_table_date < gouging_date and
                        primary_table_date < surfacing_date and
                        primary_table_date < heat_treatment_date and
                        primary_table_date < machining_date else False)
