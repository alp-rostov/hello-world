# Generated by Django 4.0.6 on 2022-07-07 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='position',
            field=models.CharField(choices=[('DI', 'Директор'), ('AD', 'Администратор'), ('CO', 'Повар'), ('CA', 'Кассир'), ('CL', 'Уборщик')], max_length=2),
        ),
    ]
