from django.contrib import admin

from my_app_0.models import Basic
from my_app_0.models import ManyToManyTo, ManyToManyFrom
from my_app_0.models import ManyToManyWithExtraFieldsTo, ManyToManyWithExtraFieldsFrom, ManyToManyWithExtraFields
from my_app_0.models import ManyToOneOne, ManyToOneMany

admin.site.register(Basic)
admin.site.register(ManyToOneOne)
admin.site.register(ManyToOneMany)
admin.site.register(ManyToManyTo)
admin.site.register(ManyToManyFrom)
admin.site.register(ManyToManyWithExtraFieldsTo)
admin.site.register(ManyToManyWithExtraFieldsFrom)
admin.site.register(ManyToManyWithExtraFields)
