# Generated by Django 2.1.7 on 2021-04-10 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0005_auto_20210313_2336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='quantidade',
        )
    ]
