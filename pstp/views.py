from django.shortcuts import render_to_response
from pstp.models import  Subject, Subheader, GradedAttr

def index(request):

    sub_dict = {}

    for subject in Subject.objects.all():
        headers_of_subject = Subheader.objects.filter(subject = subject)
        sub_dict[subject.name] = {}

        for mysubheader in headers_of_subject: 
            ga_list = GradedAttr.objects.filter(subheader = mysubheader) 
            sub_dict[subject.name][mysubheader.name] = ga_list
                
    
    return render_to_response('pstp/index.html',{
        'sub_dict': sub_dict,
    })
