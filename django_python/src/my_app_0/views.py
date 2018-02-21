from django.http import HttpResponse
from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader

from my_app_0.models import OneToManyOne


def index(request):
    my_list = [(0, "a"), (1, "b"), (2, "c")]
    template = loader.get_template('my_app_0/index.html')
    context = {
        'my_list': my_list,
    }
    return HttpResponse(template.render(context, request))

def index_shortcut(request):
    my_list = [(0, "a"), (1, "b"), (2, "c")]
    context = {
        'my_list': my_list,
    }
    return render(request, 'my_app_0/index.html', context)


def url_parameter(request, parameter_0):
    return HttpResponse("this is my_app_0 url_parameter parameter_0(%s)." % parameter_0)

def test_404(request):
    try:
        one_to_many_one = OneToManyOne.objects.get(pk=999)
    except OneToManyOne.DoesNotExist:
        raise Http404("OneToManyOne does not exist !!!")
    return render(request, 'my_app_0/test_404.html', {'one_to_many_one': one_to_many_one})

def test_404_shortcut(request):
    one_to_many_one = get_object_or_404(OneToManyOne, pk=999)
    return render(request, 'my_app_0/test_404.html', {'one_to_many_one': one_to_many_one})


