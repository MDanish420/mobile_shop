from django.contrib import admin
from product.models import product_model

@admin.register(product_model)

class product_admin(admin.ModelAdmin):
    list_display = ['id']

# Register your models here.
