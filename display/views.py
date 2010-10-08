from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context, loader

from dashboard.display.models import Spreadsheet, Student, StudentClass

from pygooglechart import PieChart2D
from pygooglechart import ScatterChart
from pylab import *
import etframes


def students(request):
    records = Student.objects.all()
    return render_to_response('display/students.html', {'students': records})

def student(request, student_id):
    record = Student.objects.get(pk=student_id)
    attn_list = [int(record.attn_sept), int(record.attn_oct), int(record.attn_nov), int(record.attn_dec), int(record.attn_jan)]
    attn_ave = sum(attn_list)/len(attn_list)
    grades = StudentClass.objects.filter(student=student_id).all()
    return render_to_response('display/student.html', {'student': record, 'attn_ave': attn_ave, 'grades': grades})

def grade(request):
    years = ['01', '02', '03', '04', '05', '06', '07', '08']
    dict_rows = {}
    for grade in sorted(years):
        dict_rows[grade] = Spreadsheet.objects.filter(grade=grade).values()
        #for row in students:
            #dict_rows[grade].append(row)
        #dict_class = {}
        #for x in dict_rows[0]:
            #dict_class[x] = []
        #for y in dict_rows:
    return render_to_response('display/grade.html', 
            {'dict_rows': dict_rows})

def graph_all(request):
    birthdays = Spreadsheet.objects.order_by('dob2').exclude(dob2='').all()
    students = []
    lang_list = [
            ('Amharic / Ethiopian', 'grey'),
            ('Arabic', 'grey'),
            ('Bengali', 'grey'),
            ('Cape Verdean', 'grey'),
            ('Creole(Haitian)', 'purple'),
            ('Dutch', 'grey'),
            ('English', 'green'),
            ('Farsi', 'grey'),
            ('French', 'red'),
            ('German', 'grey'),
            ('Nepali', 'grey'),
            ('Other', 'grey'),
            ('Portuguese', 'yellow'),
            ('Punjabi', 'grey'),
            ('Russian', 'grey'),
            ('Serbo-Croatian', 'grey'),
            ('Somali', 'grey'),
            ('Spanish', 'orange'),
            ('Swedish', 'grey'),
            ('Tamil', 'grey'),
            ('Thai', 'grey'),
            ('Tibetan', 'grey'),
            ('Tigre / Ethiopian', 'grey'),
            ('Turkish', 'grey'),
            ('Vietnamese', 'grey'),
            ]

    for student in birthdays:
        s = {}
        # Student stats
        s['dob'] = student.dob2
        s['homelang'] = student.homelang
        s['att'] = student.att2
        # English language score
        if student.g7ela:
            s['ela'] = int(student.g7ela)
        elif student.g6ela:
            s['ela'] = int(student.g6ela)
        elif student.g5ela:
            s['ela'] = int(student.g5ela)
        elif student.g4ela:
            s['ela'] = int(student.g4ela)
        else:
            s['ela'] = ''

        # Math test score
        if student.g7math:
            s['math'] = int(student.g7math)
        elif student.g6math:
            s['math'] = int(student.g6math)
        elif student.g5math:
            s['math'] = int(student.g5math)
        elif student.g4math:
            s['math'] = int(student.g4math)
        else:
            s['math'] = ''

        
        for x in lang_list:
            if s['homelang'] == x[0]:
                s['homelang'] = x[1]
            else:
                s['homelang'] = 'grey'


        if s['math'] and s['ela']:
             students.append(s)

    # Scatter graph
    x = []
    y = []
    z = []
    for s in students:
        x.append(s['math'])
        y.append(s['ela'])
        z.append(s['homelang'])



    chart = ScatterChart(500, 400, x_range=(int(sorted(x)[0] - 10), int(sorted(x)[-1]) + 10), y_range=(int(sorted(y)[0] - 10), int(sorted(y)[-1]+10)))
    chart.add_data(x)
    chart.add_data(y)
    scatter = {}
    scatter['math_x_ela'] = chart.get_url()
    

    graph = []
    graph.append(scatter)

    #scatter(x,y,c=z)
    #etframes.add_dot_dash_plot(gca(), ys=y, xs=x)



    return render_to_response('display/graph_all.html', {'students': students, 'graphs': graph })





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
