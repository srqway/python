from django.urls import path

from . import views

app_name = 'my_app_0'
urlpatterns = [
    path('', views.index, name='index'),
    path('index_shortcut', views.index_shortcut, name='index shortcut'),
    path('basic', views.basic, name='basic'),
    path('<int:parameter_0>/<int:parameter_1>/', views.url_parameter, name='url parameter'),
    path('test_404', views.test_404, name='test 404'),
    path('test_404_shortcut', views.test_404_shortcut, name='test 404 shortcut'),
    path('extends', views.extends, name='extends'),
    path('logical', views.logical, name='logical'),
    path('get', views.get, name='get'),
    path('form', views.form, name='form'),
    path('mail', views.mail, name='mail'),
    path('mass_mail', views.mass_mail, name='mass mail'),
    path('email_multi_alternatives', views.email_multi_alternatives, name='email multi alternatives'),
    path('cache', views.cache, name='cache'),
    path('list_json', views.list_json, name='list json'),
    path('dict_json', views.dict_json, name='dict json'),
]
