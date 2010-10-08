from django.db import models

class Spreadsheet(models.Model):
    hr = models.TextField(db_column=u'HR', blank=True) # Field name made lowercase. This field type is a guess.
    grade = models.TextField(db_column=u'Grade', blank=True) # Field name made lowercase. This field type is a guess.
    program = models.TextField(db_column=u'Program', blank=True) # Field name made lowercase. This field type is a guess.
    att = models.TextField(db_column=u'Att', blank=True) # Field name made lowercase. This field type is a guess.
    susp = models.TextField(db_column=u'Susp', blank=True) # Field name made lowercase. This field type is a guess.
    ela = models.TextField(db_column=u'ELA', blank=True) # Field name made lowercase. This field type is a guess.
    math = models.TextField(db_column=u'Math', blank=True) # Field name made lowercase. This field type is a guess.
    null1 = models.TextField(blank=True) # This field type is a guess.
    fname = models.TextField(db_column=u'Fname', blank=True) # Field name made lowercase. This field type is a guess.
    field = models.TextField(blank=True) # This field type is a guess.
    lname = models.TextField(db_column=u'Lname', blank=True) # Field name made lowercase. This field type is a guess.
    race = models.TextField(db_column=u'Race', blank=True) # Field name made lowercase. This field type is a guess.
    ishisp = models.TextField(db_column=u'IsHisp', blank=True) # Field name made lowercase. This field type is a guess.
    gen = models.TextField(db_column=u'Gen', blank=True) # Field name made lowercase. This field type is a guess.
    homelang = models.TextField(db_column=u'HomeLang', blank=True) # Field name made lowercase. This field type is a guess.
    sped = models.TextField(db_column=u'SpEd', blank=True) # Field name made lowercase. This field type is a guess.
    lowincome = models.TextField(db_column=u'LowIncome', blank=True) # Field name made lowercase. This field type is a guess.
    entrydate = models.TextField(db_column=u'EntryDate', blank=True) # Field name made lowercase. This field type is a guess.
    entrygr = models.TextField(db_column=u'EntryGr', blank=True) # Field name made lowercase. This field type is a guess.
    null2 = models.TextField(db_column=u'NULL2', blank=True) # Field name made lowercase. This field type is a guess.
    dob1 = models.TextField(db_column=u'DOB1', blank=True) # Field name made lowercase. This field type is a guess.
    overage = models.TextField(db_column=u'Overage', blank=True) # Field name made lowercase. This field type is a guess.
    null3 = models.TextField(db_column=u'NULL3', blank=True) # Field name made lowercase. This field type is a guess.
    gkdibels = models.TextField(db_column=u'GKDIBELS', blank=True) # Field name made lowercase. This field type is a guess.
    g1dibels = models.TextField(db_column=u'G1DIBELS', blank=True) # Field name made lowercase. This field type is a guess.
    g2dibels = models.TextField(db_column=u'G2DIBELS', blank=True) # Field name made lowercase. This field type is a guess.
    null4 = models.TextField(db_column=u'NULL4', blank=True) # Field name made lowercase. This field type is a guess.
    g3ela = models.TextField(db_column=u'G3ELA', blank=True) # Field name made lowercase. This field type is a guess.
    g4ela = models.TextField(db_column=u'G4ELA', blank=True) # Field name made lowercase. This field type is a guess.
    g5ela = models.TextField(db_column=u'G5ELA', blank=True) # Field name made lowercase. This field type is a guess.
    g6ela = models.TextField(db_column=u'G6ELA', blank=True) # Field name made lowercase. This field type is a guess.
    g7ela = models.TextField(db_column=u'G7ELA', blank=True) # Field name made lowercase. This field type is a guess.
    null5 = models.TextField(db_column=u'NULL5', blank=True) # Field name made lowercase. This field type is a guess.
    g3math = models.TextField(db_column=u'G3Math', blank=True) # Field name made lowercase. This field type is a guess.
    g4math = models.TextField(db_column=u'G4Math', blank=True) # Field name made lowercase. This field type is a guess.
    g5math = models.TextField(db_column=u'G5Math', blank=True) # Field name made lowercase. This field type is a guess.
    g6math = models.TextField(db_column=u'G6Math', blank=True) # Field name made lowercase. This field type is a guess.
    g7math = models.TextField(db_column=u'G7Math', blank=True) # Field name made lowercase. This field type is a guess.
    null6 = models.TextField(db_column=u'NULL6', blank=True) # Field name made lowercase. This field type is a guess.
    att2 = models.TextField(db_column=u'Att2', blank=True) # Field name made lowercase. This field type is a guess.
    null7 = models.TextField(db_column=u'NULL7', blank=True) # Field name made lowercase. This field type is a guess.
    susp2 = models.TextField(db_column=u'Susp2', blank=True) # Field name made lowercase. This field type is a guess.
    null8 = models.TextField(db_column=u'NULL8', blank=True) # Field name made lowercase. This field type is a guess.
    ml = models.TextField(db_column=u'ML', blank=True) # Field name made lowercase. This field type is a guess.
    eph = models.TextField(db_column=u'EPH', blank=True) # Field name made lowercase. This field type is a guess.
    b_and_g = models.TextField(db_column=u'B_AND_G', blank=True) # Field name made lowercase. This field type is a guess.
    aceit = models.TextField(db_column=u'AceIT', blank=True) # Field name made lowercase. This field type is a guess.
    hatian = models.TextField(db_column=u'Hatian', blank=True) # Field name made lowercase. This field type is a guess.
    has = models.TextField(db_column=u'HAS', blank=True) # Field name made lowercase. This field type is a guess.
    cs = models.TextField(db_column=u'CS', blank=True) # Field name made lowercase. This field type is a guess.
    aftsh = models.TextField(db_column=u'AftSh', blank=True) # Field name made lowercase. This field type is a guess.
    null9 = models.TextField(db_column=u'NULL9', blank=True) # Field name made lowercase. This field type is a guess.
    grade2 = models.TextField(db_column=u'Grade2', blank=True) # Field name made lowercase. This field type is a guess.
    exit_date = models.TextField(db_column=u'Exit_Date', blank=True) # Field name made lowercase. This field type is a guess.
    id_local = models.TextField(db_column=u'ID_Local', blank=True) # Field name made lowercase. This field type is a guess.
    id_state = models.TextField(db_column=u'ID_State', blank=True) # Field name made lowercase. This field type is a guess.
    dob2 = models.TextField(db_column=u'DOB2', blank=True) # Field name made lowercase. This field type is a guess.
    g3dibels = models.TextField(db_column=u'G3DIBELS', blank=True) # Field name made lowercase. This field type is a guess.
    g4grade = models.TextField(db_column=u'G4GRADE', blank=True) # Field name made lowercase. This field type is a guess.
    g5grade = models.TextField(db_column=u'G5GRADE', blank=True) # Field name made lowercase. This field type is a guess.
    g6grade = models.TextField(db_column=u'G6GRADE', blank=True) # Field name made lowercase. This field type is a guess.
    yog = models.TextField(db_column=u'YOG', blank=True) # Field name made lowercase. This field type is a guess.
    question1 = models.TextField(blank=True) # This field type is a guess.
    homeroom = models.TextField(db_column=u'Homeroom', blank=True) # Field name made lowercase. This field type is a guess.
    entryyear = models.TextField(db_column=u'EntryYear', blank=True) # Field name made lowercase. This field type is a guess.
    cohort = models.TextField(db_column=u'Cohort', blank=True) # Field name made lowercase. This field type is a guess.
    g3ela1 = models.TextField(db_column=u'G3ELA1', blank=True) # Field name made lowercase. This field type is a guess.
    g4ela1 = models.TextField(db_column=u'G4ELA1', blank=True) # Field name made lowercase. This field type is a guess.
    g4ela2 = models.TextField(db_column=u'G4ELA2', blank=True) # Field name made lowercase. This field type is a guess.
    g5ela1 = models.TextField(db_column=u'G5ELA1', blank=True) # Field name made lowercase. This field type is a guess.
    g5ela2 = models.TextField(db_column=u'G5ELA2', blank=True) # Field name made lowercase. This field type is a guess.
    g6ela1 = models.TextField(db_column=u'G6ELA1', blank=True) # Field name made lowercase. This field type is a guess.
    g6ela2 = models.TextField(db_column=u'G6ELA2', blank=True) # Field name made lowercase. This field type is a guess.
    g7ela1 = models.TextField(db_column=u'G7ELA1', blank=True) # Field name made lowercase. This field type is a guess.
    g7ela2 = models.TextField(db_column=u'G7ELA2', blank=True) # Field name made lowercase. This field type is a guess.
    g3math2 = models.TextField(db_column=u'G3Math2', blank=True) # Field name made lowercase. This field type is a guess.
    g4math1 = models.TextField(db_column=u'G4Math1', blank=True) # Field name made lowercase. This field type is a guess.
    g4math2 = models.TextField(db_column=u'G4Math2', blank=True) # Field name made lowercase. This field type is a guess.
    g5math1 = models.TextField(db_column=u'G5Math1', blank=True) # Field name made lowercase. This field type is a guess.
    g5math2 = models.TextField(db_column=u'G5Math2', blank=True) # Field name made lowercase. This field type is a guess.
    g4grade1 = models.TextField(db_column=u'G4GRADE1', blank=True) # Field name made lowercase. This field type is a guess.
    g5grade1 = models.TextField(db_column=u'G5GRADE1', blank=True) # Field name made lowercase. This field type is a guess.
    g6grade1 = models.TextField(db_column=u'G6GRADE1', blank=True) # Field name made lowercase. This field type is a guess.
    g4grade2 = models.TextField(db_column=u'G4GRADE2', blank=True) # Field name made lowercase. This field type is a guess.
    g5grade2 = models.TextField(db_column=u'G5GRADE2', blank=True) # Field name made lowercase. This field type is a guess.
    g6grade2 = models.TextField(db_column=u'G6GRADE2', blank=True) # Field name made lowercase. This field type is a guess.
    x21st_cent = models.TextField(db_column=u'x21st_Cent', blank=True) # Field name made lowercase. This field type is a guess.
    b_and_gclub = models.TextField(db_column=u'B_AND_GClub', blank=True) # Field name made lowercase. This field type is a guess.
    eph1 = models.TextField(db_column=u'EPH1', blank=True) # Field name made lowercase. This field type is a guess.
    mysticlc = models.TextField(db_column=u'MysticLC', blank=True) # Field name made lowercase. This field type is a guess.
    ymca = models.TextField(db_column=u'YMCA', blank=True) # Field name made lowercase. This field type is a guess.
    homeworkhelp = models.TextField(db_column=u'HomeworkHelp', blank=True) # Field name made lowercase. This field type is a guess.
    hasclub = models.TextField(db_column=u'HASClub', blank=True) # Field name made lowercase. This field type is a guess.
    hasreading = models.TextField(db_column=u'HASReading', blank=True) # Field name made lowercase. This field type is a guess.
    hasmath = models.TextField(db_column=u'HASMath', blank=True) # Field name made lowercase. This field type is a guess.
    hasesl = models.TextField(db_column=u'HASESL', blank=True) # Field name made lowercase. This field type is a guess.
    schdayreading = models.TextField(db_column=u'SchDayReading', blank=True) # Field name made lowercase. This field type is a guess.
    schdaymath = models.TextField(db_column=u'SchDayMath', blank=True) # Field name made lowercase. This field type is a guess.
    schdayell = models.TextField(db_column=u'SchDayELL', blank=True) # Field name made lowercase. This field type is a guess.
    spedela = models.TextField(db_column=u'SpEDELA', blank=True) # Field name made lowercase. This field type is a guess.
    spedmath = models.TextField(db_column=u'SpEdMath', blank=True) # Field name made lowercase. This field type is a guess.
    program1 = models.TextField(db_column=u'Program1', blank=True) # Field name made lowercase. This field type is a guess.
    hbase = models.TextField(db_column=u'HBase', blank=True) # Field name made lowercase. This field type is a guess.
    def __unicode__(self):
        return self.grade + ' ' + self.grade + ' ' + self.homeroom
    class Meta:
        db_table = u'school'


class Student(models.Model):
    attn_sept = models.IntegerField()
    attn_oct = models.IntegerField()
    attn_nov = models.IntegerField()
    attn_dec = models.IntegerField()
    attn_jan = models.IntegerField()
    grade = models.IntegerField()
    homelang = models.TextField()

class StudentClass(models.Model):
    student = models.ForeignKey(Student)
    class_name = models.TextField()
    class_teach = models.TextField()
    class_goal = models.IntegerField()
    class_credits = models.IntegerField()
    class_grade = models.IntegerField()

class Supporter(models.Model):
    student = models.ForeignKey(Student)
    name = models.TextField()
    relationship = models.TextField()
