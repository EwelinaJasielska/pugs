from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import logging
logger = logging.getLogger('django.server')

# Create your views here.
def index(request):
	logger.error('xxx index')
	return lista(request)

def nowy(request):
	logger.error('xxx nowy')
	return render(request, 'nowy.html')

@csrf_exempt
def dodaj(request):
	logger.error('xxx dodaj')
	imie = request.POST.get("imie", "")
	kolor = request.POST.get("kolor", "")
	wiek = request.POST.get("wiek", "")
	from app.models import Pug
	Pug.Insert(imie, kolor, wiek)
	return lista(request)

@csrf_exempt
def skasuj(request):
	logger.error('xxx skasuj')
	return lista(request)

def lista(request):
	logger.error('xxx lista')
	from app.models import Pug
	mopsy = Pug.objects.all()
	return render(request, 'index.html', context={'mopsy': mopsy})