from django.db import models
from product.models import product_model

class category_model(models.Model):
    category_name = models.CharField(max_length = 20)
    product_fk = models.ForeignKey(product_model , on_delete = models.CASCADE , null = True)


    def __str__(self) -> str:
        return self.category_name

# Create your models here.
