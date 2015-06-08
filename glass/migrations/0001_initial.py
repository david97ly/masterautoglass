# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('telefono1', models.CharField(max_length=500)),
                ('telefono2', models.CharField(max_length=500)),
                ('telefono3', models.CharField(max_length=500)),
                ('correo1', models.CharField(max_length=500)),
                ('correo2', models.CharField(max_length=500)),
                ('correo3', models.CharField(max_length=500)),
                ('fax1', models.CharField(max_length=500)),
                ('fax2', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Fotos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=500)),
                ('ruta', models.ImageField(upload_to=b'photos')),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=500)),
                ('subtitulo', models.CharField(max_length=500)),
                ('informacion', models.CharField(max_length=100)),
                ('foto', models.ForeignKey(to='glass.Fotos')),
            ],
        ),
        migrations.CreateModel(
            name='Mensajeb',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mensaje', models.CharField(max_length=500)),
                ('subensaje', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=500)),
                ('informacion', models.CharField(max_length=100)),
                ('foto', models.ForeignKey(to='glass.Fotos')),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mensaje', models.CharField(max_length=500)),
                ('submensaje', models.CharField(max_length=500)),
                ('alida', models.BooleanField(default=True)),
                ('foto', models.ForeignKey(to='glass.Fotos')),
            ],
        ),
    ]
