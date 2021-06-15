from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import logging
logger = logging.getLogger('django.server')

# Create your views here.
def index(request):
	logger.error('...index')
	return lista(request)

def nowy(request):
	logger.error('...nowy')
	return render(request, 'nowy.html')

@csrf_exempt
def dodaj(request):
	logger.error('...dodaj')
	imie = request.POST.get("imie", "")
	kolor = request.POST.get("kolor", "")
	wiek = request.POST.get("wiek", "")
	logger.error('...dodaj imie:'+imie+ ' kolor:'+kolor+' wiek:'+wiek)
	from app.models import Pug
	try:
		p = Pug(imie = imie, kolor = kolor, wiek = wiek)
		p.save(force_insert=True)
	except:
		logger.error('...insert ERROR')
	return lista(request)

@csrf_exempt
def skasuj(request):
	logger.error('...skasuj')
	return lista(request)

def lista(request):
	from app.models import Pug
	mopsy = Pug.objects.all()
	for m in mopsy:
		logger.info('... id:'+m.id+' imie:'+m.imie+' kolor'+m.kolor+' wiek:'+m.wiek)
	return render(request, 'index.html', context={'mopsy': mopsy})