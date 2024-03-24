from django.contrib import admin
from category.models import category_model

@admin.register(category_model)

class category_admin(admin.ModelAdmin):
    list_display = ['id' , 'category_name']



# Register your models here.
