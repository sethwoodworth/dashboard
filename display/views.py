from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context, loader

from display.models import Spreadsheet, Student, StudentClass

import calendar
import datetime
import random
from random import choice, gauss, randint, uniform

#from pygooglechart import PieChart2D, ScatterChart, StackedVerticalBarChart
#from pylab import *
#import etframes

def load_demographics(request):
    """
    Read locally hosted csv files from Somerville's X2 export and feeds them 
    into the django database.  This enables us to reload on new export or to 
    fix errors from a static platonic ideal.
    """
    # TODO: rename, not just touching upon demographics anymore
    from django.shortcuts import redirect
    import csv
    import decimal

    from display.models import Demographics
    from display.models import DIEBELS
    from display.models import Mcasela
    from display.models import Mcasmath

    ## Clean out old tables and reimport from scratch
    Demographics.objects.all().delete()
    DIEBELS.objects.all().delete()

    ## Load the Demographics table
    file = open('./data/HEA_DEMO.txt', 'r')
    reader = csv.reader(file)
    for student in reader:
        d = Demographics()
        d.fname         = student[0]
        d.mname         = student[1]
        d.lname         = student[2]
        d.id1           = int(student[3])
        d.id2           = int(student[4])
        d.grade_level   = student[5]
        d.grad_year     = int(student[6])
        d.homeroom      = student[7]
        d.gender        = student[8]
        d.birth_date    = student[9]
        d.home_lang     = student[10]
        d.lang_level    = student[11]
        d.race          = student[12]
        # skip d.other1 = student[13]
        # skip \N       = student[14]
        d.frl           = student[15]   
        if student[16] != '\N':
            d.attendance    = decimal.Decimal(student[16])
        d.other2        = student[17]
        d.enrollment    = student[18]
        d.save()
    file.close()

    ## Load District Entry and Exit info
    file1 = open('./data/HEA_ENTRY.txt', 'r')
    file2 = open('./data/HEA_EXIT.txt', 'r')
    entry_reader = csv.reader(file1)
    exit_reader = csv.reader(file2)
    for record in entry_reader:
        # TODO: make these one update statement
        sid1 = record[1]
        years = 2011 - int(record[5][:4])
        Demographics.objects.filter(id1=sid1).update(entry_date=record[5])
        Demographics.objects.filter(id1=sid1).update(years_at=years)
    for record in exit_reader:
        sid1 = record[1]
        Demographics.objects.filter(id1=sid1).update(exit_date=record[5])
        Demographics.objects.filter(id1=sid1).update(withdrawl=record[3])
    file1.close()
    file2.close()
        
    ## Load Attendence for Year to Date
    file = open('./data/HEA_ATT_YTD.txt', 'r')
    reader = csv.reader(file)
    for record in reader:
        Demographics.objects.filter(id1=record[0]).update(missed_days=record[1])

    ## DIBELS tests
    grades          = ['KF', '01', '02', '03']
    test_numbers    = ['1', '2', '3']
    for grade in grades:
        for test in test_numbers:
            filename = './data/HEA_DIBELS' + test + '_G' + grade + '.txt'
            file = open(filename, 'r')
            reader = csv.reader(file)
            for test in reader:
                demo = Demographics.objects.filter(id1=test[1]).all()[0]
                dd = DIEBELS()
                dd.f_id1 = demo
                dd.test_name = test[3]
                dd.date = test[4]
                dd.result = test[7]
                dd.save()

    ## MCAS English Language Arts (ELA)
    grades = ['03', '04', '05', '06', '07', '08']
    for grade in grades:
        filename = './data/HEA_ELA_G' + grade + '.txt'
        file = open(filename, 'r')
        reader = csv.reader(file)
        for test in reader:
            demo = Demographics.objects.filter(id1=test[1]).all()[0]
            ela = Mcasela()
            ela.f_id1 = demo
            ela.test_name = test[3]
            ela.date = test[4]
            if test[7] != '\N':
                ela.scaled_score = test[7]
            if test[8] != '\N':
                ela.raw_score = test[8]
            ela.level = test[9]
            ela.save()

    ## MCAS Math
    grades = ['03', '04', '05', '06', '07', '08']
    for grade in grades:
        filename = './data/HEA_MATH_G' + grade + '.txt'
        file = open(filename, 'r')
        reader = csv.reader(file)
        for test in reader:
            demo = Demographics.objects.filter(id1=test[1]).all()[0]
            math = Mcasmath()
            math.f_id1 = demo
            math.test_name = test[3]
            math.date = test[4]
            if test[7] != '\N':
                math.scaled_score = test[7]
            if test[8] != '\N':
                math.raw_score = test[8]
            math.level = test[9]
            math.save()

    return redirect('/real')

def real_grade(request):
    from display.models import Demographics
    students = Demographics.objects.all()
    students_all = []
    for student in students:
        # setup data structure to return
        student_d = {'data': student, 'tests': {}}

        # Return diebel test info
        diebels = student.diebels_set.order_by('date').reverse()
        student_d['tests']['diebels'] = diebels
        # Return mcas_ela test info
        mcas_ela = student.mcasela_set.order_by('date').reverse()
        student_d['tests']['ela'] = mcas_ela
        # Return mcas_math test info
        mcas_math = student.mcasmath_set.order_by('date').reverse()
        student_d['tests']['math'] = mcas_math

        students_all.append(student_d)

        
    return render_to_response('display/real_admin.html', {'students': students, 'students_all': students_all})


def students(request):
    records = Student.objects.all()
    return render_to_response('display/students.html', {'students': records})

def student(request, student_id):
    # query general student data
    record = Student.objects.get(pk=student_id)

    ## Attendance
    # grab attendance-month summaries from general data
    attn_list = [int(record.attn_sept), int(record.attn_oct), int(record.attn_nov), int(record.attn_dec), int(record.attn_jan)]
    attn_ave = sum(attn_list)/len(attn_list)
    attn_q = [a-50 for a in attn_list]

    ## Grades
    # Retreive and calculate this-semester grade data and goals
    grades = StudentClass.objects.filter(student=student_id).all()
    goal_list = []
    for goal in grades:
        goal_list.append(int(goal.class_goal))
    grade_goal = sum(goal_list)/7
    grade_list = []
    for grade in grades:
        grade_list.append(int(grade.class_grade))
    grade_ave = sum(grade_list)/7

    ## Credits
    credits = {}
    credits['passed'] = ['eng1', 'alge1a', 'pre-bio', 'ushis1', 'health']
    credits['f_total'] = sum([x.class_credits for x in grades])



    return render_to_response('display/student.html', {'student': record, 'attn_ave': attn_ave, 'grades': grades, 'grade_goal': grade_goal, 'grade_ave': grade_ave})

def attn_month(month_number):
    if month_number > 9:
        year = 2010
    else:
        year = 2010
    mo = calendar.monthrange(year, month_number)[1] 
    # implement this later, grabs the # of weekdays in a month, not really important
    #weekdays = len([date for date in range(1,mo) if calendar.weekday(year, month_number, date) < 5])
    missed = round(abs(gauss(0,3)))
    att = mo - missed
    return (att, mo, missed)

def fake_student(request):
    name = {'first_name': choice(['Agustin','Theresa','Salim','Philemon','Nilsa','Katherinne']),
            'last_name': choice(['Brody','Fils-Aime','Leib','Ojeda','O\'Keefe','Oppedisano'])}
    grade = choice([('9th',2014),('10th',2015)])

    att_month = {'September': attn_month(9),
                'October': attn_month(10),
                'November': attn_month(11),
                'December': attn_month(12),
                'January': attn_month(1)}
    att = { 'average': int(round(sum([att_month[key][0] for key in att_month])/sum([att_month[key][1] for key in att_month])*100)),
            'months': att_month }

    scores = [ 
        {'class_credits': 5,
          'class_goal': 82,
          'class_grade': 100 - int(round(abs(gauss(0,19)))),
          'class_name': u'Pre-Biology',
          'class_teach': u'Ms. Tsoi'},
         {'class_credits': 5,
          'class_goal': 92,
          'class_grade': 100 - int(round(abs(gauss(0,19)))),
          'class_name': u'Algebra 1A',
          'class_teach': u'Mr. Morgan'},
         {'class_credits': 5,
          'class_goal': 87,
          'class_grade': 100 - int(round(abs(gauss(0,19)))),
          'class_name': u'US History 1',
          'class_teach': u'Ms. Dedieu'},
         {'class_credits': 5,
          'class_goal': 90,
          'class_grade': 100 - int(round(abs(gauss(0,25)))),
          'class_name': u'French 1',
          'class_teach': u'Mme. Lawrence'},
         {'class_credits': 5,
          'class_goal': 87,
          'class_grade': 100 - int(round(abs(gauss(0,17)))),
          'class_name': u'English 1',
          'class_teach': u'Ms. Mattos'},
         {'class_credits': 3,
          'class_goal': 80,
          'class_grade': 100 - int(round(abs(gauss(0,20)))),
          'class_name': u'Health Edu.',
          'class_teach': u'Ms. Flynn'},
         {'class_credits': 3,
          'class_goal': 80,
          'class_grade': 100 - int(round(abs(gauss(0,20)))),
          'class_name': u'Intro. Guitar',
          'class_teach': u'Ms. Sears'}]
    grades = {'average': sum([x['class_grade'] for x in scores])/len(scores),
                'scores': scores}

    math = {
        'sept': randint(210,250),
        'jan': randint(210,250),
        'apr': randint(210,250)}
    ela = {
        'sept': randint(210,250),
        'jan': randint(210,250),
        'apr': randint(210,250)}

    return render_to_response('display/fake.html', {'name': name, 'grade': grade, 'att': att, 'grades': grades, 'math': math, 'ela': ela})

def issp(request, student_id=1):
    # Return what existing that we hvae
    #record = Student.objects.get(pk=student_id)
    #the_class = StudentClass.objects.filter(student=record.pk)[0]
    #adv_teacher = the_class.class_teach # guessing first() teacher the Advisor
    adv_teacher = "Mrs. Robinson"
        

    # Random values as placeholders for database stores
    math = {
        'sept': randint(210,250),
        'jan': randint(210,250),
        'apr': randint(210,250)}
    ela = {
        'sept': randint(210,250),
        'jan': randint(210,250),
        'apr': randint(210,250)}

    return render_to_response('display/issp.html', {'today': datetime.datetime.now(), 'advisor': adv_teacher, 'math': math, 'ela': ela})

def grade(request):
    years = ['01', '02', '03', '04', '05', '06', '07', '08']
    dict_rows = {}
    d_list = []
    for grade in sorted(years):
        d_list.append(Spreadsheet.objects.filter(grade=grade).values())
    for year in d_list:
        for student in year.values():
            student['att'] = student['att']

        #for row in students:
            #dict_rows[grade].append(row)
        #dict_class = {}
        #for x in dict_rows[0]:
            #dict_class[x] = []
        #for y in dict_rows:
    return render_to_response('display/grade.html', 
            {'dict_rows': d_list, 'grades': years})

def w_choice(lst):
    n = uniform(0, 1)
    for item, weight in lst:
        if n < weight:
            break
        n = n - weight
    return item

def a_fake(count=1):
    student_list = []
    for x in range(count):
        student = {}
        student['first_name'] = choice(['Adam', 'Alex', 'Beth', 'Chris', 'Salim', 'Gianna', 'Yahaira', 'Tenzin', 'Marisa'])
        student['last_name'] = choice(['Perez', 'Ricci', 'Mathews', 'Mechem', 'Fonseca', 'Killoren', 'Haley', 'DeMattia'])
        student['gen'] = choice(['M','F'])
        student['homeroom'] = choice(['HEA 313', 'HEA 105', 'HEA 316', 'HEA 105', 'HEA 301', 'HEA 219', 'HEA 200'])
        student['att'] = int(round(abs(gauss(0,9)))) # Attendance
        student['tardy'] = int(round(abs(gauss(0,9))))
        student['homelang'] = w_choice([
          ('Amharic',         0.01), 
          ('Arabic',          0.01), 
          ('Bengali',         0.03), 
          ('Creole(Haitian)', 0.10), 
          ('Portuguese',      0.15), 
          ('Spanish',         0.15), 
          ('Dutch',           0.02), 
          ('English',         0.7)])
        student['yearsat'] = random.randint(1,6)
        student['mapmath1'] = randint(150,260)
        student['mapmath2'] = int(round(abs(gauss(0,11)))) 
        student['mapreading1'] = randint(150,260)
        student['mapreading2'] = int(round(abs(gauss(0,11)))) 
        student['ward'] = randint(1,7)
        student['ell'] = choice([True, False])
        if student['ell'] == True:
          student['mepa_r'] = random.randint(10,30)
          student['mepa_w'] = random.randint(10,30)
        student['iep'] = choice([False, False, False, False, False, False, True])
        student['afterschool'] = set( [w_choice([("B&G", 0.5), ("Peabody", 0.05), ("Mystic", 0.15), ("", .30)]), w_choice([("B&G", 0.1), ("Peabody", 0.05), ("Mystic", 0.15), ("", .50)])])

        student_list.append(student)
    return student_list

def fake_grade(request):
    from collections import Counter

    students = a_fake(100)

    # prepare language graph data
    data = [s['homelang'] for s in students]
    l_cnt = Counter()
    for word in data:
      l_cnt[word] += 1
    lang_graph = [dict(l_cnt)]

    # prepare math x read graph data
    mvr_data = [[s['mapmath2'], s['mapreading2']] for s in students]

    return render_to_response('display/admin.html', {'students': students, 'lang': lang_graph, 'math_v_read': mvr_data})

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
