from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from polls.models import Poll

# Create your views here.

def index(request):
	#return HttpResponse("Hello, world. You're at the Poll index!")
	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	# template = loader.get_template('polls/index.html')
	# context = RequestContext(request, {
	# 	'latest_poll_list': latest_poll_list,
	# })
	# return HttpResponse(template.render(context))
	context = {'latest_poll_list': latest_poll_list}
	return render(request, 'polls/index.html', context)

def detail(request, poll_id):
	# try:
	# 	poll = Poll.objects.get(pk=poll_id)
	# except Poll.DoesNotExist:
	# 	raise Http404
	poll = get_object_or_404(Poll, pk=poll_id)
	return render(request, 'polls/detail.html', {'poll': poll})

def results(request, poll_id):
	return HttpResponse("You're looking at the results of poll {0}".format(poll_id))

def vote(request, poll_id):
	return HttpResponse("You're voting on poll {0}".format(poll_id))