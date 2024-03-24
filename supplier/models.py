from django.db import models



class supplier_model(models.Model):
    name = models.CharField(max_length =10)
    contact = models.CharField(max_length = 20)
    address = models.TextField( )


    def __str__(self):
        return self.name
# Create your models here.
