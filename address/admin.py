from django.contrib import admin

# Register your models here.
from .models import Address


class maddress(admin.ModelAdmin):
    list_display = ('__str__','id','village','union')


admin.site.register(Address,maddress)

