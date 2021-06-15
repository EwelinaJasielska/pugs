from django.db import models

# Create your models here.
class Pug(models.Model):
	imie = models.CharField(max_length=100)
	kolor = models.CharField(max_length=100)
	wiek = models.CharField(max_length=100)

	def __str__(self):
		return self.imie
	
	def Insert(imie, kolor, wiek):
		p = Pug(imie = imie, kolor = kolor, wiek = wiek)
		p.save