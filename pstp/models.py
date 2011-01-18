from django.db import models

class Subject(models.Model):
    #TODO
    # - make last_update inform the last time this was saved 
    name = models.CharField(max_length = 20) 
#    last_update = models.DateTimeField('last updated')
    def __unicode__(self): 
        return self.name

class Subheader(models.Model): 
    name = models.CharField(max_length= 20) 
    subject = models.ForeignKey(Subject)
    def __unicode__(self):
        return self.name 

class Grade(models.Model): 
    grade = models.CharField(max_length = 30) 
    def __unicode__(self):
        return self.grade

class GradedAttr(models.Model):
    subject = models.ForeignKey(Subject) 
    subheader = models.ForeignKey(Subheader) 
    rubric_row = models.CharField(max_length = 150)  
    rubric_desc = models.TextField()
    grade = models.ForeignKey(Grade)
    def __unicode__(self): 
        return self.rubric_row

class CommentField(models.Model): 
    username = models.CharField(max_length = 20) 
    subject = models.ForeignKey(Subject)
    input = models.TextField() 
    def __unicode__(self):
            return self.username 

