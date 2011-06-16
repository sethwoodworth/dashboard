from django.conf.urls.defaults import *
from django.contrib import admin
from display import views
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'display.views.fake_grade'),
    (r'^real/$', 'display.views.real_grade'),
    (r'^load/$', 'display.views.load_demographics'),
    (r'^pstp/$', 'pstp.views.index'),
    (r'^dashboard/', include('display.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'static'}),
)
