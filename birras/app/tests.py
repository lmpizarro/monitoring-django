from django.test import TestCase
from app.services import boxs_to_buy
# Create your tests here.
from birras.settings import TEMP_MIN, TEMP_MAX

class ServiceTest(TestCase):

    def test_boxs_to_buy(self):
        
        boxs = boxs_to_buy(24, 100)
        
        assert boxs == 17
        
