# Generated by Django 4.2.4 on 2023-08-11 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_remove_products_first_li_remove_products_second_li_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='productbrand',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
