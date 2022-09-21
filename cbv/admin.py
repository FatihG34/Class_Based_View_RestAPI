from django.contrib import admin

from cbv.models import Country, People

# Register your models here.
admin.site.register(People)
admin.site.register(Country)