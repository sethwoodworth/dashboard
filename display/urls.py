from django.conf.urls.defaults import *
from dashboard.display.models import Spreadsheet

urlpatterns = patterns('dashboard.display.views',
    (r'^$', 'index'),
    (r'^grade', 'fake_grade'),
    (r'^graphs', 'graph_all'),
    (r'^stats', 'stats'),
    (r'^students', 'students'),
    (r'^student/issp', 'issp'),
    (r'^student/(?P<student_id>\d+)', 'student'),
    (r'^student/fake', 'fake_student'),
    (r'^sample', 'sample'),
    (r'^(\d+)', 'detail'),
)
