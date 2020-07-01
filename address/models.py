from django.db import models

class Address(models.Model):
    d_name = models.CharField(max_length=30)
    village = models.IntegerField()
    union = models.IntegerField()
    populetions = models.IntegerField()

    def __str__(self):
        return self.d_name
