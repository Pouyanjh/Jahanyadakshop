# Generated by Django 4.2.4 on 2023-09-29 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_alter_products_options_order_orderproduct_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
    ]
