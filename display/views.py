from django.shortcuts import render_to_response
from dashboard.display.models import Spreadsheet

def index(request):
     = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('polls/index.html', {'latest_poll_list': latest_poll_list})

