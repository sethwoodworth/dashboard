from django.conf.urls.defaults import *
from dashboard.display.models import Spreadsheet

urlpatterns = patterns('dashboard.display.views',
    (r'^$', 'index'),
    (r'^grade', 'grade'),
    (r'^graphs', 'graph_all'),
    (r'^stats', 'stats'),
    (r'^students', 'students'),
    (r'^student/(?P<student_id>\d+)', 'student'),
    (r'^sample', 'sample'),
    (r'^(\d+)', 'detail'),
)
