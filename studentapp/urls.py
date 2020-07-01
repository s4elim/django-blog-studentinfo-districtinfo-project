from django.urls import path, include

from studentapp.views import studentlist, studentdetails

urlpatterns = [
    path('list/',studentlist, name='studentlist'),
    path('details/<int:s_id>', studentdetails, name='studentdetails'),
]

