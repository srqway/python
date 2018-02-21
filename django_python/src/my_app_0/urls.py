from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:parameter_0>/', views.url_parameter, name='url parameter'),
]