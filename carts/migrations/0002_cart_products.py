# Generated by Django 3.2.4 on 2021-06-10 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_image'),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(through='carts.CartProducts', to='products.Product'),
        ),
    ]
