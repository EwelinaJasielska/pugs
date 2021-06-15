from django.db import models
import logging
logger = logging.getLogger('django.server')

# Create your models here.
class Pug(models.Model):
	imie = models.CharField(max_length=100)
	kolor = models.CharField(max_length=100)
	wiek = models.CharField(max_length=100)

	def __str__(self):
		return self.imie
	