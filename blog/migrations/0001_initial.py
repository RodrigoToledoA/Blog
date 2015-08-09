# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='T\xedtulo de la Categor\xeda')),
                ('descripcion', models.CharField(max_length=256, verbose_name='Descripci\xf3n de la Categor\xeda')),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('celu', models.CharField(max_length=100, verbose_name='Telefono')),
                ('mail', models.CharField(max_length=100, verbose_name='Mail')),
                ('mensaje', models.TextField(verbose_name='Mensaje')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha del Post')),
            ],
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100, verbose_name='T\xedtulo')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha del Post')),
                ('resumen', models.CharField(max_length=512, verbose_name='Resumen')),
                ('contenido', models.TextField(verbose_name='Contenido')),
                ('published', models.BooleanField(default=True, verbose_name='Publicado?')),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('categoria', models.ManyToManyField(to='blog.Categoria')),
            ],
            options={
                'ordering': ['-fecha'],
                'verbose_name': 'Entrada',
                'verbose_name_plural': 'Todas las Entradas',
            },
        ),
        migrations.CreateModel(
            name='Mensajes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('mensaje', models.TextField(verbose_name='Mensaje')),
                ('published', models.BooleanField(default=False, verbose_name='Publicado?')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha del Mensaje')),
                ('published_in', models.ForeignKey(to='blog.Entrada')),
            ],
            options={
                'ordering': ['-fecha'],
                'verbose_name': 'Mensaje',
                'verbose_name_plural': 'Todos los mensajes',
            },
        ),
    ]
