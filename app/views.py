from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'index.html')

def dodaj(request):
	return render(request, 'dodaj.html')
