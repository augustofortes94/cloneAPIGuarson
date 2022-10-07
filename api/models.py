from django.db import models


class Command(models.Model):
    name = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=50)
    text = models.CharField(max_length=500, null=True, blank=True, default=None)
    parameter1 = models.CharField(max_length=50, null=True, blank=True, default=None)
    parameter2 = models.CharField(max_length=50, null=True, blank=True, default=None)


class Weapon(models.Model):
    command = models.ForeignKey(Command, on_delete=models.CASCADE, related_name="commands")
    category = models.CharField(max_length=50)
    name = models.CharField(max_length=50, unique=True)
    muzzle = models.CharField(max_length=100, null=True, blank=True, default=None)
    barrel = models.CharField(max_length=100, null=True, blank=True, default=None)
    laser = models.CharField(max_length=100, null=True, blank=True, default=None)
    optic = models.CharField(max_length=100, null=True, blank=True, default=None)
    stock = models.CharField(max_length=100, null=True, blank=True, default=None)
    underbarrel = models.CharField(max_length=100, null=True, blank=True, default=None)
    magazine = models.CharField(max_length=100, null=True, blank=True, default=None)
    ammunition = models.CharField(max_length=100, null=True, blank=True, default=None)
    reargrip = models.CharField(max_length=100, null=True, blank=True, default=None)
    perk = models.CharField(max_length=100, null=True, blank=True, default=None)
    perk2 = models.CharField(max_length=100, null=True, blank=True, default=None)
    alternative = models.CharField(max_length=512, null=True, blank=True, default=None)
    alternative2 = models.CharField(max_length=512, null=True, blank=True, default=None)


class Lobby(models.Model):
    mode = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50, unique=True)
    map = models.CharField(max_length=50, null=True, blank=True, default=None)
