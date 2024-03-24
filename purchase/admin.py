from django.contrib import admin
from purchase.models import purchase_model


@admin.register(purchase_model)

class purchase_admin(admin.ModelAdmin):
    list_display = ['id']

# Register your models here.
