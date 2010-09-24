from django.shortcuts import render_to_response
from dashboard.display.models import Spreadsheet
from django.http import HttpResponse
from django.template import Context, loader


def login(request):
    return HttpResponse("Hello, world. You're at the dashboard login.")

def detail(request, student_id):
    try:
        s = Spreadsheet.objects.get(id=student_id)
    except Spreadsheet.DoesNotExist:
        raise Http404
    return render_to_response('dashboard/student_detail.html', {'student': s})

def stats(request):
    try:
        a = Spreadsheet.objects.all()
        columns = {}
        for key in a.values()[0].keys():
            columns[key] = []
        for d in a.values():
            for k in d.keys():
                columns[k].append(d[k])
    except Spreadsheet.DoesNotExist:
        raise Http404
    return render_to_response('dashboard/student_stats.html', columns)

def sample(request):
    return render_to_response('dashboard/sample.html')

def index(request):
    a = Spreadsheet.objects.all()
    columns = {}
    for key in a.values()[0].keys():
        columns[key] = []
    for d in a.values():
        for k in d.keys():
            columns[k].append(d[k])
    t = loader.get_template('dashboard/student_stats.html')
    c = Context({
                'data_columns': columns,
                })
    return HttpResponse(t.render(c))
