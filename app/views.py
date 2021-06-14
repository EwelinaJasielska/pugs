from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'index.html')

def nowy(request):
	return render(request, 'nowy.html')

def dodaj(request):
	return render(request, 'index.html')

def skasuj(request):
	return render(request, 'index.html')
