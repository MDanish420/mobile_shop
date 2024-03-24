from django.db import models
# from category.models import category_model


class product_model(models.Model):
    mobile_name = models.CharField(max_length = 15)
    mobile_model = models.CharField(max_length = 15)
    EMEI = models.CharField(max_length = 25)
    category = models.CharField(max_length = 20)
    color = models.CharField(max_length = 15) 



    def __str__(self):
        return self.mobile_name

# Create your models here.
