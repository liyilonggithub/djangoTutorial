from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Poll

# Create your views here.

def index(request):
	#return HttpResponse("Hello, world. You're at the Poll index!")
	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	output = ', '.join([p.question for p in latest_poll_list])
	return HttpResponse(output)

def detail(request, poll_id):
	return HttpResponse("You're looking at poll {0}".format(poll_id))

def results(request, poll_id):
	return HttpResponse("You're looking at the results of poll {0}".format(poll_id))

def vote(request, poll_id):
	return HttpResponse("You're voting on poll {0}".format(poll_id))