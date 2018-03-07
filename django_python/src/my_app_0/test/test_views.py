from django.test import Client
from django.test import TestCase
from django.urls.base import reverse


class Test(TestCase):

    def setUp(self):
        super(Test, self).setUp()
        self.clinet = Client(enforce_csrf_checks=True)

    def tearDown(self):
        super(Test, self).tearDown()

    def test_index(self):
        url = reverse('my_app_0:index')
        response = self.clinet.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_basic(self):
        url = reverse('my_app_0:basic')
        response = self.clinet.get(url)
        self.assertEqual(response.status_code, 200)

    def test_url_parameter(self):
        url = reverse('my_app_0:url parameter', args=(0, 1,))
        response = self.clinet.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"parameter_0(0), parameter_1(1).")
    
    def test_test_404(self):
        url = reverse('my_app_0:test 404')
        response = self.clinet.get(url)
        self.assertEqual(response.status_code, 404)   
        
    def test_cache(self):
        url = reverse('my_app_0:cache')
        response_0 = self.clinet.get(url)
        response_1 = self.clinet.get(url)
        self.assertEqual(response_0.content, response_1.content)   
