from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views import generic

from polls.models import Poll, Choice

# Create your views here.

# def index(request):
# 	#return HttpResponse("Hello, world. You're at the Poll index!")
# 	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
# 	# template = loader.get_template('polls/index.html')
# 	# context = RequestContext(request, {
# 	# 	'latest_poll_list': latest_poll_list,
# 	# })
# 	# return HttpResponse(template.render(context))
# 	context = {'latest_poll_list': latest_poll_list}
# 	return render(request, 'polls/index.html', context)

# def detail(request, poll_id):
# 	# try:
# 	# 	poll = Poll.objects.get(pk=poll_id)
# 	# except Poll.DoesNotExist:
# 	# 	raise Http404
# 	poll = get_object_or_404(Poll, pk=poll_id)
# 	return render(request, 'polls/detail.html', {'poll': poll})

# def results(request, poll_id):
# 	poll = get_object_or_404(Poll, pk=poll_id)
# 	return render(request, 'polls/result.html', {'poll': poll})

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """Return the last five published polls."""
        return Poll.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/result.html'

def vote(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	try:
		select_choice = p.choice_set.get(pk=request.POST['choice'])
	except(KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			'poll': p,
			'error_message': "You didn't select a choice",
		})
	else:
		select_choice.votes += 1
		select_choice.save()

		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))