# Generated by Django 5.0.3 on 2024-03-23 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='supplier_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('contact', models.CharField(max_length=20)),
                ('address', models.TextField()),
            ],
        ),
    ]