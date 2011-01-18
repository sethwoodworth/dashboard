from pstp.models import Subject, GradedAttr, Subheader 
from django.contrib import admin

class SubheaderInline(admin.StackedInline):
    model = Subheader
    extra = 1

class GradesInline(admin.StackedInline):
    model = GradedAttr
    extra = 6


class SubjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',                  {'fields':['name']}),
    ]
    inlines = [SubheaderInline]
    inlines = [GradesInline]

admin.site.register(Subject, SubjectAdmin )
