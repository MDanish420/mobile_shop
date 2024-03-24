# Generated by Django 5.0.3 on 2024-03-24 08:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('purchase', '0001_initial'),
        ('supplier', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase_model',
            name='sname',
        ),
        migrations.AlterField(
            model_name='purchase_model',
            name='productfk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product_model', verbose_name='Prouduact'),
        ),
        migrations.AlterField(
            model_name='purchase_model',
            name='supplierfk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='supplier.supplier_model', verbose_name='Supplier'),
        ),
    ]