from django.contrib import admin
from studentapp.models import Student

class Substu(admin.ModelAdmin):
    list_display = ("__str__",'name','gender','date_at','comment')

admin.site.register(Student,Substu)