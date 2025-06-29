# Generated by Django 5.2.1 on 2025-05-30 22:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Held',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rasse', models.CharField(max_length=100)),
                ('kultur', models.CharField(max_length=100)),
                ('profession', models.CharField(max_length=100)),
                ('lebenspunkte', models.IntegerField(default=30)),
                ('ausdauer', models.IntegerField(default=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ausruestung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('typ', models.CharField(max_length=50)),
                ('held', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ausruestung', to='helden_app.held')),
            ],
        ),
        migrations.CreateModel(
            name='Attribut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('wert', models.IntegerField()),
                ('held', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attribute', to='helden_app.held')),
            ],
        ),
        migrations.CreateModel(
            name='Talent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('wert', models.IntegerField()),
                ('held', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='talente', to='helden_app.held')),
            ],
        ),
    ]
