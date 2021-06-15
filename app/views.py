from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
	return lista(request)

def nowy(request):
	return render(request, 'nowy.html')

@csrf_exempt
def dodaj(request):
	imie = request.POST.get("imie", "")
	kolor = request.POST.get("kolor", "")
	wiek = request.POST.get("wiek", "")
	from app.models import Pug
	Pug.Insert(imie, kolor, wiek)
	return lista(request)

@csrf_exempt
def skasuj(request):
	return lista(request)

def lista(request):
	from app.models import Pug
	mopsy = Pug.objects.all()
	return render(request, 'index.html', context={'mopsy': mopsy})