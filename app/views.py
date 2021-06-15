from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
	return render(request, 'index.html')

def nowy(request):
	return render(request, 'nowy.html')

@csrf_exempt
def dodaj(request):
	imie = request['imie']
	kolor = request['kolor']
	wiek = request['wiek']
	from app.models import Pug
	Pug.Insert(imie, kolor, wiek)
	return render(request, 'index.html')

@csrf_exempt
def skasuj(request):
	return render(request, 'index.html')
