from django.shortcuts import render, redirect
import threading

from .models import *

from . import detect, trash
from .detect import detect
from .trash import trash

# Create your views here.

def home(request):

	if request.method=="POST":
		if request.POST.get('Rcnumber'):
			rcnumber = request.POST.get('Rcnumber')
			vehicle = None
			message = 1

			try:
				vehicle = Vehicle.objects.get( registration_no = rcnumber)
			except:
				message = 0

			context = {'vehicle':vehicle,'message':message}
			return render(request,'detection/theft_detection.html',context)
			
	return render(request, 'detection/theft_detection.html')


t = threading.Thread(target = trash)
t.start()