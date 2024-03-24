from django.db import models
from supplier.models import supplier_model
from product.models import product_model



class purchase_model(models.Model):
    supplierfk = models.ForeignKey(supplier_model , on_delete = models.CASCADE , null = True , verbose_name = 'Supplier')
    productfk = models.ForeignKey(product_model , on_delete = models.CASCADE , null = True , verbose_name = 'Prouduact')
    price = models.FloatField()
    quantity = models.IntegerField()
    total_amount = models.FloatField()
    
    


# Create your models here.
