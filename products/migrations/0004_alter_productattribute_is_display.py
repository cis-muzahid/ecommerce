# Generated by Django 4.2.10 on 2024-02-20 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_is_disable_productattribute_is_display'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productattribute',
            name='is_display',
            field=models.BooleanField(default=True),
        ),
    ]
