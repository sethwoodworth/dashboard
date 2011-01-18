from django.shortcuts import render_to_response
from pstp.models import  Subject, Subheader, GradedAttr

def index(request):

    sub_dict = {}
    head_dict = {}

    for subject in Subject.objects.all():
        x = Subheader.objects.filter(subject = subject)
        sub_dict[subject.name] = x

    for subheader in Subheader.objects.all():
        x = GradedAttr.objects.filter(subheader = subheader)
        head_dict[subheader.name] = x
# The next line would be used if we were going to automagically generate commentfields. As it stands, I am just going to hardcode them in index.html.     
#    for subject in CommentField.objects.all
    
    return render_to_response('pstp/index.html',{
        'sub_dict': sub_dict,
        'head_dict': head_dict,
    })
