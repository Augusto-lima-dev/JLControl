# Generated by Django 3.1.2 on 2021-02-26 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0002_auto_20210226_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='traje',
            name='ativo',
            field=models.CharField(choices=[('nao', 'Não'), ('sim', 'Sim')], default=1, max_length=100),
        ),
        migrations.AlterField(
            model_name='traje',
            name='codigo',
            field=models.CharField(max_length=20),
        ),
    ]
