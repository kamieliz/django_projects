from django.shortcuts import HttpResponse
from django.template import RequestContext, loader

from polls.models import Poll

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)
def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)
    
def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll)
    
def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_idp)

# Create your views here.
