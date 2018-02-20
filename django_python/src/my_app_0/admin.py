from django.contrib import admin

# Register your models here.
from .models import OneToManyOne, OneToManyMany

admin.site.register(OneToManyOne)
admin.site.register(OneToManyMany)