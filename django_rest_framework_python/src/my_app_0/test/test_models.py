import unittest

from my_app_0.models import Basic
from my_app_0.serializers import BasicSerializer


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testName(self):
        basic = Basic()
        basic.id = 1
        basic.big_integer_field = 2
        basic.save()
        serializer = BasicSerializer(basic)
        self.assertEqual(serializer.data.__str__(), "{'id': 1, 'big_integer_field': 2, 'boolean_field': False, 'char_field': None, 'choice_field': '', 'date_field': None, 'date_time_field': None, 'decimal_field': None, 'duration_field': None, 'email_field': None, 'file_field': None, 'file_path_field': None, 'float_field': None, 'image_field': None, 'integer_field': None, 'generic_ip_address_field': None, 'null_boolean_field': None, 'positive_integer_field': None, 'positive_small_integer_field': None, 'slug_field': None, 'small_integer_field': None, 'text_field': None, 'time_field': None, 'url_field': None, 'uuid_field': None}")

