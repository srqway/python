from django.db.models.aggregates import Count
from django.test import TestCase

from my_app_0.models import Basic, ManyToOneOne, ManyToOneMany, ManyToManyTo, \
    ManyToManyFrom


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
        
    def test_basic_values_list(self):
        Basic.objects.create(id=0, char_field="aaa")
        Basic.objects.create(id=1, char_field="bbb")
        Basic.objects.create(id=2, char_field="ccc")        
        basics = Basic.objects.values_list("char_field", flat=True)
        self.assertEqual(basics.query.__str__(), 'SELECT "my_app_0_basic"."char_field" FROM "my_app_0_basic"') 
        
    def test_basic_values_list_as_list(self):
        Basic.objects.create(id=0, char_field="aaa")
        Basic.objects.create(id=1, char_field="bbb")
        Basic.objects.create(id=2, char_field="ccc")        
        basics = Basic.objects.values_list("char_field", flat=True)
        self.assertEqual(basics.query.__str__(), 'SELECT "my_app_0_basic"."char_field" FROM "my_app_0_basic"') 
        
    def test_basic_values(self):
        Basic.objects.create(id=0, char_field="aaa")
        Basic.objects.create(id=1, char_field="bbb")
        Basic.objects.create(id=2, char_field="ccc")        
        basics = list(Basic.objects.values("id", "char_field"))
        self.assertEqual(basics.__str__(), "[{'id': 0, 'char_field': 'aaa'}, {'id': 1, 'char_field': 'bbb'}, {'id': 2, 'char_field': 'ccc'}]")  
        
    def test_basic_values_list_as_dict(self):
        Basic.objects.create(id=0, char_field="aaa")
        Basic.objects.create(id=1, char_field="bbbb")
        Basic.objects.create(id=2, char_field="ccc")        
        basics = list(Basic.objects.values_list("id", "char_field"))
        self.assertEqual(basics.__str__(), "[(0, 'aaa'), (1, 'bbbb'), (2, 'ccc')]")  
        
    def test_basic_query_str(self):       
        basics = Basic.objects.values_list("id", "char_field")
        self.assertEqual(basics.query.__str__(), 'SELECT "my_app_0_basic"."id", "my_app_0_basic"."char_field" FROM "my_app_0_basic"')
        
    def test_basic_count(self):   
        Basic.objects.create(id=0, char_field="aaa")
        Basic.objects.create(id=1, char_field="aaa")
        Basic.objects.create(id=2, char_field="ccc")  
        basics = list(Basic.objects.all().values("char_field").annotate(count=Count('*')).values('char_field', 'count'))
        self.assertEqual(basics.__str__(), "[{'char_field': 'aaa', 'count': 2}, {'char_field': 'ccc', 'count': 1}]")
    
    def test_basic_defer(self):   
        Basic.objects.create(id=0, char_field="aaa")
        basics = Basic.objects.all().defer("big_integer_field")
        self.assertEqual(basics.query.__str__(), 'SELECT "my_app_0_basic"."id", "my_app_0_basic"."boolean_field", "my_app_0_basic"."char_field", "my_app_0_basic"."choice_field", "my_app_0_basic"."date_field", "my_app_0_basic"."date_time_field", "my_app_0_basic"."decimal_field", "my_app_0_basic"."duration_field", "my_app_0_basic"."email_field", "my_app_0_basic"."file_field", "my_app_0_basic"."file_path_field", "my_app_0_basic"."float_field", "my_app_0_basic"."image_field", "my_app_0_basic"."integer_field", "my_app_0_basic"."generic_ip_address_field", "my_app_0_basic"."null_boolean_field", "my_app_0_basic"."positive_integer_field", "my_app_0_basic"."positive_small_integer_field", "my_app_0_basic"."slug_field", "my_app_0_basic"."small_integer_field", "my_app_0_basic"."text_field", "my_app_0_basic"."time_field", "my_app_0_basic"."url_field", "my_app_0_basic"."uuid_field" FROM "my_app_0_basic"')
        
    def test_basic_only(self):   
        Basic.objects.create(id=0, char_field="aaa")
        basics = Basic.objects.all().only("big_integer_field")
        self.assertEqual(basics.query.__str__(), 'SELECT "my_app_0_basic"."id", "my_app_0_basic"."big_integer_field" FROM "my_app_0_basic"')
        
    def test_many_to_one_select_related(self):
        one = ManyToOneOne.objects.create(id=0, char_field="one") 
        ManyToOneMany.objects.create(id=0, char_field="many", many_to_one_one=one) 
        ManyToOneMany.objects.create(id=1, char_field="many", many_to_one_one=one) 
        manys = ManyToOneMany.objects.all().select_related('many_to_one_one')
        self.assertEqual(manys.count(), 2)  
        
    def test_many_to_one_prefetch_related(self):
        one = ManyToOneOne.objects.create(id=0, char_field="one") 
        ManyToOneMany.objects.create(id=0, char_field="many", many_to_one_one=one) 
        ManyToOneMany.objects.create(id=1, char_field="many", many_to_one_one=one) 
        ones = ManyToOneOne.objects.all().prefetch_related('manytoonemany_set')
        self.assertEqual(ones[0].manytoonemany_set.count(), 2)  
        
    def test_many_to_many_prefetch_related(self):
        self.generate_many_to_many_data()
        tos = ManyToManyTo.objects.all().prefetch_related('manytomanyfrom_set')
        self.assertEqual(tos[0].manytomanyfrom_set.count(), 3) 
        
    def generate_many_to_many_data(self):
        for to_id in range(3):
            to = ManyToManyTo.objects.create(id=to_id, char_field="to") 
            for from_id in range(3):
                from_, created = ManyToManyFrom.objects.get_or_create(id=from_id, char_field="from") 
                to.manytomanyfrom_set.add(from_)
