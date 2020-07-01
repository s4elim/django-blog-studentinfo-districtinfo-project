from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    gender= models.CharField(max_length=6)
    mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    date_at = models.DateField(auto_now=True)
    comment = models.TextField()

    def __str__(self):
        return self.name
