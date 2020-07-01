from django.shortcuts import render

from .models import Student


def studentlist(request):
    valu = Student.objects.all()
    contex = {
        'students': valu
    }
    return render(request, 'student/studentlist.html', contex)

def studentdetails(request,s_id):
    valu = Student.objects.get(id=s_id)
    contex = {
        'student':valu
    }
    return render(request, 'student/studentdetails.html',contex)