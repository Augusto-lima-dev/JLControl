# Generated by Django 2.1.7 on 2021-04-10 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0006_auto_20210410_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='data_entrega',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
