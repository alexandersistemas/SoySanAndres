# Generated by Django 4.0.5 on 2022-07-01 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Agencia', '0003_tipoparentesco_integrante'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='Password',
            field=models.CharField(default='nopws', max_length=45),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Direccion',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='Telefono1',
            field=models.CharField(max_length=45, null=True),
        ),
    ]