# Generated by Django 4.0.5 on 2022-07-01 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('idCiudad', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('idCliente', models.AutoField(primary_key=True, serialize=False)),
                ('NumeroDocumento', models.IntegerField()),
                ('Nombres', models.CharField(max_length=100)),
                ('Apellidos', models.CharField(max_length=100)),
                ('FechaNacimiento', models.DateField()),
                ('Direccion', models.CharField(max_length=45)),
                ('Telefono2', models.CharField(max_length=45)),
                ('Telefono1', models.CharField(max_length=45)),
                ('Correo', models.EmailField(max_length=254)),
                ('FechaCreado', models.DateTimeField(auto_now_add=True)),
                ('idCiudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agencia.ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Cupon',
            fields=[
                ('idCupon', models.AutoField(primary_key=True, serialize=False)),
                ('FechaCreado', models.DateTimeField(auto_now_add=True)),
                ('Porcentaje', models.IntegerField()),
                ('Cupon', models.CharField(max_length=45)),
                ('FechaInicio', models.DateField()),
                ('FechaFin', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('idEstado', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('idImagen', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=45)),
                ('FechaCreado', models.DateTimeField(auto_now_add=True)),
                ('Ruta', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('idPais', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='PlanTuristico',
            fields=[
                ('idPlan', models.AutoField(primary_key=True, serialize=False)),
                ('Descripcion', models.TextField(max_length=255)),
                ('Capacidad', models.IntegerField(null=True)),
                ('Nombre', models.CharField(max_length=100)),
                ('PrecioDolar', models.IntegerField()),
                ('PrecioPeso', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Promocion',
            fields=[
                ('idPromocion', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=45)),
                ('Descripcion', models.TextField(max_length=255)),
                ('FechaInicio', models.DateField()),
                ('FechaFin', models.DateField()),
                ('PrecioPeso', models.IntegerField()),
                ('PrecioDolar', models.IntegerField()),
                ('FechaCreado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Promotor',
            fields=[
                ('idPromotor', models.AutoField(primary_key=True, serialize=False)),
                ('NumeroDocumento', models.IntegerField()),
                ('Nombres', models.CharField(max_length=45)),
                ('Apellidos', models.CharField(max_length=45)),
                ('PorcentajeComision', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('idTipoDocumento', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPQRS',
            fields=[
                ('idTipoPQRS', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('FechaCreado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('idTransaccion', models.AutoField(primary_key=True, serialize=False)),
                ('FechaCreado', models.DateTimeField(auto_now_add=True)),
                ('Valor', models.IntegerField()),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agencia.cliente')),
                ('idCupon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Agencia.cupon')),
                ('idEstado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agencia.estado')),
                ('idPromotor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Agencia.promotor')),
            ],
        ),
        migrations.CreateModel(
            name='TransaccionPromocion',
            fields=[
                ('idTransaccionPromocion', models.AutoField(primary_key=True, serialize=False)),
                ('idPromocion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agencia.promocion')),
                ('idTransaccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agencia.transaccion')),
            ],
        ),
        migrations.CreateModel(
            name='TransaccionPlan',
            fields=[
                ('idTransaccionPlan', models.AutoField(primary_key=True, serialize=False)),
                ('idPlan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agencia.planturistico')),
                ('idTransaccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agencia.transaccion')),
            ],
        ),
        migrations.AddField(
            model_name='promotor',
            name='idTipoDocumento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agencia.tipodocumento'),
        ),
        migrations.CreateModel(
            name='PromocionImagen',
            fields=[
                ('idPromocionImagen', models.AutoField(primary_key=True, serialize=False)),
                ('idImagen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agencia.imagen')),
                ('idPromocion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agencia.promocion')),
            ],
        ),
        migrations.CreateModel(
            name='PQRS',
            fields=[
                ('idPQRS', models.AutoField(primary_key=True, serialize=False)),
                ('FechaCreado', models.DateTimeField(auto_now_add=True)),
                ('Descripcion', models.TextField(max_length=255)),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agencia.cliente')),
                ('idTipoPQRS', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agencia.tipopqrs')),
            ],
        ),
        migrations.CreateModel(
            name='PlanImagen',
            fields=[
                ('idPlanImagen', models.AutoField(primary_key=True, serialize=False)),
                ('idImagen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agencia.imagen')),
                ('idPlan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agencia.planturistico')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='idTipoDocumento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agencia.tipodocumento'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='idPais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Agencia.pais'),
        ),
    ]
