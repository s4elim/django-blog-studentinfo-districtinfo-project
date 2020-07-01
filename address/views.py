from django.shortcuts import render

from .models import Address


def district(request):
    valu = Address.objects.all()
    contex = {
        'district': valu
    }
    return render(request,'address/district.html', contex)

def districtinfo(request, d_id):
    valu = Address.objects.get(id = d_id)
    contex = {
        'districtinfo': valu
    }
    return render(request,'address/districtinfo.html', contex)