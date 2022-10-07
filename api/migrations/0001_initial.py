# Generated by Django 4.0.5 on 2022-09-20 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('category', models.CharField(max_length=50)),
                ('text', models.CharField(blank=True, default=None, max_length=500, null=True)),
                ('parameter1', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('parameter2', models.CharField(blank=True, default=None, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('map', models.CharField(blank=True, default=None, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('muzzle', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('barrel', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('laser', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('optic', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('stock', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('underbarrel', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('magazine', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('ammunition', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('reargrip', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('perk', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('perk2', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('alternative', models.CharField(blank=True, default=None, max_length=512, null=True)),
                ('alternative2', models.CharField(blank=True, default=None, max_length=512, null=True)),
                ('command', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commands', to='api.command')),
            ],
        ),
    ]