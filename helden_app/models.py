from django.db import models
from django.contrib.auth.models import User

class Held(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    rasse = models.CharField(max_length=100)
    kultur = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    lebenspunkte = models.IntegerField(default=30)
    ausdauer = models.IntegerField(default=30)

    def __str__(self):
        return self.name

class Attribut(models.Model):
    held = models.ForeignKey(Held, related_name='attribute', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    wert = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.wert})"

class Talent(models.Model):
    held = models.ForeignKey(Held, related_name='talente', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    wert = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.wert})"

class Ausruestung(models.Model):
    held = models.ForeignKey(Held, related_name='ausruestung', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    typ = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.typ}: {self.name}"

