# Generated by Django 4.1.6 on 2023-06-05 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='session_key',
            field=models.CharField(max_length=32, null=True),
        ),
    ]