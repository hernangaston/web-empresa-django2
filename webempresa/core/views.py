from django.shortcuts import render

# Create your views here.

def home(request):
	title = "Inicio"
	d = dict(title=title)
	return render(request, "core/index.html", d)

def about(request):
	title = "Historia"
	d = dict(title=title)
	return render(request, "core/about.html", d)

def store(request):
	title = "Visitanos"
	d = dict(title=title)
	return render(request, "core/store.html", d)

