from django.contrib import admin
from supplier.models import supplier_model

@admin.register(supplier_model)


class supplier_admin(admin.ModelAdmin):
    list_display = ['id']

# Register your models here.
