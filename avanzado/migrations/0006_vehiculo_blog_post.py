# Generated by Django 4.1.1 on 2022-12-12 18:17

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avanzado', '0005_delete_mascota_alter_vehiculo_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='blog_post',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]