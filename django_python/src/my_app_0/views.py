from django.core.mail import send_mail, send_mass_mail
from django.core.mail.message import EmailMultiAlternatives
from django.http import HttpResponse
from django.http.response import Http404, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.utils import timezone
from django.views.decorators.cache import cache_page

from django_python import settings
from my_app_0.forms import MyForm
from my_app_0.models import Basic


def index(request):
    template = loader.get_template('my_app_0/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def index_shortcut(request):
    context = {}
    return render(request, 'my_app_0/index.html', context)

  
def basic(request):
    basic = Basic()
    basic.date_time_field = timezone.now()
    template = loader.get_template('my_app_0/basic.html')
    context = {
        'basic': basic,
    }
    return HttpResponse(template.render(context, request))


def url_parameter(request, parameter_0, parameter_1):
    return HttpResponse("parameter_0(%s), parameter_1(%s)." % (parameter_0, parameter_1))


def test_404(request):
    try:
        one_to_many_one = Basic.objects.get(pk=999)
    except Basic.DoesNotExist:
        raise Http404("OneToManyOne does not exist !!!")
    return render(request, 'my_app_0/test_404.html', {'one_to_many_one': one_to_many_one})


def test_404_shortcut(request):
    one_to_many_one = get_object_or_404(Basic, pk=999)
    return render(request, 'my_app_0/test_404.html', {'one_to_many_one': one_to_many_one})


def extends(request):
    context = {
        "title" : "my_title",
        "content" : "my_content"
    }
    return render(request, 'my_app_0/extends_1.html', context)


def logical(request):
    my_list = [(0, "a"), (1, "b"), (2, "c")]
    template = loader.get_template('my_app_0/logical.html')
    context = {
        'my_list': my_list,
    }
    return HttpResponse(template.render(context, request))


def get(request):
    a = request.GET.get("a", 0)
    b = request.GET.get("b", 0)
    result = int(a) + int(b)
    return HttpResponse("%s + %s = %d" % (a, b, result))


def form(request):
    if request.method == 'POST':
        my_form = MyForm(request.POST)
        if my_form.is_valid():
            a = my_form.cleaned_data['a']
            b = my_form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))
    else:
        my_form = MyForm()
    return render(request, 'my_app_0/form.html', {'my_form': my_form})


def mail(request):
    send_mail('subject of mail', 'message', settings.DEFAULT_FROM_EMAIL, ['thank.hsiehpinghan@gmail.com'])
    return HttpResponse("send mail finished.")


def mass_mail(request):
    mail_0 = ('subject of mail_0', 'message', settings.DEFAULT_FROM_EMAIL, ['thank.hsiehpinghan@gmail.com'])
    mail_1 = ('subject of mail_1', 'message', settings.DEFAULT_FROM_EMAIL, ['thank.hsiehpinghan@gmail.com'])
    send_mass_mail((mail_0, mail_1))
    return HttpResponse("send mass mail finished.")


def email_multi_alternatives(request):
    mail = EmailMultiAlternatives('subject of email_multi_alternatives', 'text message', settings.DEFAULT_FROM_EMAIL, ['thank.hsiehpinghan@gmail.com'])
    mail.attach_alternative("<p><strong>html</strong> message</p>", "text/html")
    mail.send()
    return HttpResponse("send email multi alternatives finished.")


@cache_page(60)
def cache(request):
    return HttpResponse(timezone.now())


def list_json(request):
    list_ = [0, 1, 2]
    return JsonResponse(list_, safe=False)

 
def dict_json(request):
    dict_ = {'key_0': 'value_0', 'key_1': 'value_1'}
    return JsonResponse(dict_)
