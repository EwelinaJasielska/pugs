from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import logging
logger = logging.getLogger('django.server')

# Create your views here.
def index(request):
	logger.info('...index')
	return lista(request)

def nowy(request, error = ""):
	logger.info('...nowy')
	return render(request, 'nowy.html', context = {'error':error})

@csrf_exempt
def dodaj(request):
	logger.info('...dodaj')
	imie = request.POST.get("imie", "")
	kolor = request.POST.get("kolor", "?")
	wiek = request.POST.get("wiek", "?")
	if not imie:
		return nowy(request, 'Imie mopsa nie moze byc puste !')
	from app.models import Pug
	try:
		p = Pug(imie = imie, kolor = kolor, wiek = wiek)
		p.save(force_insert=True)
		logger.info('...dodano mopsa: imie:'+imie+ ' kolor:'+kolor+' wiek:'+wiek)
	except:
		logger.error('...insert ERROR')
	return lista(request)

def skasuj(request, id = 0):
	logger.info('...skasuj')
	if id==0:
		logger.info('...skasuj ERROR')
		return lista(request, "Nie udało się usunąć mopsa !")
	from app.models import Pug
	pug = Pug.objects.get(id = id) 
	pug.delete()
	return lista(request)

def lista(request, error = ""):
	from app.models import Pug
	mopsy = Pug.objects.all()
	for m in mopsy:
		logger.info('... id:'+str(m.id)+' imie:'+m.imie+' kolor'+m.kolor+' wiek:'+m.wiek)
	return render(request, 'index.html', context={'mopsy': mopsy, 'error': error})