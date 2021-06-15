from django.db import models

# Create your models here.
class Pug(models.Model):
	name = models.CharField(max_length=100)
	kolor = models.CharField(max_length=100)
	age = models.CharField(max_length=100)