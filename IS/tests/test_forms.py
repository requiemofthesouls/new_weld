from django.test import TestCase

from IS.forms import PrimaryTableForm


# Create your tests here.
class MyTests(TestCase):
    def test_forms(self):
        form_data = {
            'number': '124412532',
            'letter': 'HE111BC',
            'received_stamp_date': '',
            'customer': '',
            'scheme': True,
        }
        form = PrimaryTableForm(data=form_data)
        self.assertTrue(form.is_valid())
