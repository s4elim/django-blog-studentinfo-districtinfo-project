from django.urls import path

from .views import district, districtinfo

urlpatterns = [
    path('district/', district, name = 'list'),
    path('details/<int:d_id>', districtinfo, name = 'info'),
]