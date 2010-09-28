from django.shortcuts import render_to_response
from dashboard.display.models import Spreadsheet
from django.http import HttpResponse
from django.template import Context, loader
from pygooglechart import PieChart2D


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

def grade(request):
    years = ['01', '02', '03', '04', '05', '06', '07', '08']
    dict_rows = {}
    for grade in years:
        dict_rows[grade] = []
        students = Spreadsheet.objects.filter(grade=grade).values()
        for row in students:
            dict_rows[grade].append(row)
        #dict_class = {}
        #for x in dict_rows[0]:
            #dict_class[x] = []
        #for y in dict_rows:
    return render_to_response('dashboard/grade.html', {'dict_rows': dict_rows})






def index(request):
    a = Spreadsheet.objects.all()
    columns = {}

    for key in a.values()[0].keys():
        columns[key] = []
    for d in a.values():
        for k in d.keys():
            columns[k].append(d[k])
    kcount = {} 
    for k in columns.keys():
        kcount[k] = {}
        for i in set(columns[k]):
            kcount[k][i] = columns[k].count(i)

    pie_list = ['race', 'grade', 'program', 'homelang', 'sped']
    bar_list = ['lowincome', 'dob1', 'susp2', 'att']


    graphs = {} 
    # Generate PieGraphs
    for field in kcount.keys():
        labels = []
        values = []
        position = 0
        for tuple in kcount[field]:
            values.append(kcount[field][tuple])
        total = sum(values)
        for label in kcount[field]:
            if label:
                labels.append(str(label) + ' ' + str( kcount[field][label] * 100 / total) + '%')
                position =+ 1
            else:
                #lables.append('null' + ' ' + str( kcount[field][tuple] * 100 / total) + '%')
                del values[ position ]
                position =+ 1
        l = []
        v = []
        dd = kcount[field]
        for x in sorted(dd, key=lambda dd: dd[1]):
            l.append(x[0])
            v.append(x[1])
        list = zip(l,v)

        if pie_list.__contains__(field):
            chart = PieChart2D(500,250)
            chart.add_data(v)
            chart.set_pie_labels(l)
            chart.set_title(field)
            graphs[field] = chart.get_url()

        if bar_list.__contains__(field):
            chart = BarChart(500,250)

            b.set_bar_width = 15
            b.set_bar_spacing = 5
            b.set_group_spacing = 15
            b.set_colours(['4d89f9',])


            chart.add_data(values)
            chart.set_pie_labels(labels)
            chart.set_title(field)
            graphs[field] = chart.get_url()

    # Generate BarGraphs
    for field in bar_list:
        l = []
        v = []
        dd = kcount[field]
        for x in sorted(dd, key=lambda dd: dd[1]):
            l.append(x[0])
            v.append(x[1])
        list = zip(l,v)

        chart = foo


    t = loader.get_template('dashboard/student_stats.html')
    c = Context({
                'data_columns': graphs,
                })
    return HttpResponse(t.render(c))
