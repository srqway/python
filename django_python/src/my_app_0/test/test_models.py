from django.test import TestCase

from my_app_0.models import Basic


class Test(TestCase):

    def setUp(self):
        super(Test, self).setUp()

    def tearDown(self):
        super(Test, self).tearDown()

    def test_basic_create_and_get(self):
        id_value = 0
        big_integer_field_value = 1
        Basic.objects.create(id=id_value, big_integer_field=big_integer_field_value)
        basic = Basic.objects.get(big_integer_field=big_integer_field_value)
        self.assertEqual(basic.big_integer_field, big_integer_field_value)

    def test_basic_get_or_create(self):
        id_value = 0
        big_integer_field_value = 1
        Basic.objects.create(id=id_value, big_integer_field=big_integer_field_value)
        basic = Basic.objects.get(big_integer_field=big_integer_field_value)
        self.assertEqual(basic.big_integer_field, big_integer_field_value)

    def test_basic_all(self):
        Basic.objects.create(id=0, big_integer_field=10)
        Basic.objects.create(id=1, big_integer_field=11)
        Basic.objects.create(id=2, big_integer_field=12)
        basics = Basic.objects.all()
        self.assertEqual(basics.count(), 3)
        
    def test_basic_all_slice(self):
        Basic.objects.create(id=0, big_integer_field=10)
        Basic.objects.create(id=1, big_integer_field=11)
        Basic.objects.create(id=2, big_integer_field=12)
        basics = Basic.objects.all()[:2]
        self.assertEqual(basics.count(), 2)
        
    def test_basic_filter(self):
        big_integer_field_value = 1
        Basic.objects.create(id=0, big_integer_field=big_integer_field_value)
        basics = Basic.objects.filter(big_integer_field=big_integer_field_value)
        self.assertEqual(basics.count(), 1)  
        
    def test_basic_exclude(self):
        big_integer_field_value = 1
        Basic.objects.create(id=0, big_integer_field=big_integer_field_value)
        basics = Basic.objects.exclude(big_integer_field=big_integer_field_value)
        self.assertEqual(basics.count(), 0)   

    def test_basic_filter_regex(self):
        Basic.objects.create(id=0, char_field="123abc456")
        Basic.objects.create(id=1, char_field="123ABC456")
        Basic.objects.create(id=2, char_field="123aBc456")        
        basics = Basic.objects.filter(char_field__regex=".*aBc.*")
        self.assertEqual(basics.count(), 1)   
        
    def test_basic_exclude_regex(self):
        Basic.objects.create(id=0, char_field="123abc456")
        Basic.objects.create(id=1, char_field="123ABC456")
        Basic.objects.create(id=2, char_field="123aBc456")        
        basics = Basic.objects.exclude(char_field__regex=".*aBc.*")
        self.assertEqual(basics.count(), 2)     
