# Generated by Django 3.0.8 on 2020-09-30 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obstetricia', '0003_auto_20200909_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orden_medica_parto',
            name='orden_diez',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='orden_medica_parto',
            name='orden_nueve',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='orden_medica_parto',
            name='orden_ocho',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='orden_medica_parto',
            name='orden_seis',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='orden_medica_parto',
            name='orden_siete',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
