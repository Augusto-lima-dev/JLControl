# Generated by Django 3.2 on 2021-05-10 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0008_auto_20210509_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='telefone',
            field=models.BigIntegerField(),
        ),
    ]
