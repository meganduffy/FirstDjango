from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
	return render(request, "FirstDjango/home.html", 
		{"current_date": datetime.datetime.now()})

def contact(request):
	return render(request, "FirstDjango/contact.html")

def about(request):
	return render(request, "FirstDjango/about.html")