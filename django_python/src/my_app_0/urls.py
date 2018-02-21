from django.urls import path

from . import views

app_name = 'my_app_0'
urlpatterns = [
    path('', views.index, name='index'),
    path('index_shortcut', views.index_shortcut, name='index'),
    path('<int:parameter_0>/', views.url_parameter, name='url parameter'),
    path('test_404', views.test_404, name='test 404'),
    path('test_404_shortcut', views.test_404_shortcut, name='test 404 shortcut'),
]
