from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import logging
logger = logging.getLogger('django.server')

# Create your views here.
def index(request):
	logger.info('...index')
	return lista(request)

def nowy(request):
	logger.info('...nowy')
	return render(request, 'nowy.html')

@csrf_exempt
def dodaj(request):
	logger.info('...dodaj')
	imie = request.POST.get("imie", "")
	kolor = request.POST.get("kolor", "?")
	wiek = request.POST.get("wiek", "?")
	if not imie:
		from django.contrib import messages
		messages.info(request, 'Imie mopsa nie moze byc puste !!!')
		return lista(request, messages)
	from app.models import Pug
	try:
		p = Pug(imie = imie, kolor = kolor, wiek = wiek)
		p.save(force_insert=True)
		logger.info('...dodano mopsa: imie:'+imie+ ' kolor:'+kolor+' wiek:'+wiek)
	except:
		logger.error('...insert ERROR')
	return lista(request)

@csrf_exempt
def skasuj(request):
	logger.info('...skasuj')
	return lista(request)

def lista(request, messages):
	from app.models import Pug
	mopsy = Pug.objects.all()
	for m in mopsy:
		logger.info('... id:'+str(m.id)+' imie:'+m.imie+' kolor'+m.kolor+' wiek:'+m.wiek)
	return render(request, 'index.html', context={'mopsy': mopsy, 'messages': messages})