from django.contrib import admin

from my_app_0.models import OneToManyOne, OneToManyMany, ManyToManyFrom, \
    ManyToManyTo, OneToOneFrom, OneToOneTo

admin.site.register(OneToManyOne)
admin.site.register(OneToManyMany)
admin.site.register(ManyToManyFrom)
admin.site.register(ManyToManyTo)
admin.site.register(OneToOneFrom)
admin.site.register(OneToOneTo)
