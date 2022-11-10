# Generated by Django 4.1.1 on 2022-10-23 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avanzado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=20)),
                ('propietario', models.CharField(max_length=20)), 
                ('modelo', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=20)),
                ('cant_puertas', models.IntegerField()),
                ('color', models.CharField(max_length=20)),
                ('chasis', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='mascota',
            name='fecha_nacimiento',
            field=models.DateField(verbose_name=0),
        ),
    ]
