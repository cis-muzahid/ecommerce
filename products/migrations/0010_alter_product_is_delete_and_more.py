# Generated by Django 4.2.10 on 2024-02-22 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_category_is_delete_productattribute_is_delete_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='productattribute',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='productspecification',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
    ]
