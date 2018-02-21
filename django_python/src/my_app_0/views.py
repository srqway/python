from django.http import HttpResponse


def index(request):
    return HttpResponse("this is my_app_0 index.")


def url_parameter(request, parameter_0):
    return HttpResponse("this is my_app_0 url_parameter parameter_0(%s)." % parameter_0)
