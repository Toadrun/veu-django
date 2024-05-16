from django.db import models


# Create your models here.
class Student(models.Model):
    gender_choice = (('Man', 'Man'), ('Women', 'Women'))
    sno = models.IntegerField(db_column='SNo', primary_key=True, null=False)  # student number
    name = models.CharField(db_column='SName', max_length=100, null=False)  # name
    gender = models.CharField(db_column='Gender', max_length=100, choices=gender_choice)
    birthday = models.CharField(db_column='Birthday', max_length=100, null=False)
    mobile = models.CharField(db_column='Mobile', max_length=100)
    email = models.CharField(db_column='Email', max_length=100)
    address = models.CharField(db_column='Address', max_length=200)
    image = models.CharField(db_column='Image', max_length=200, null=True)

    class Meta:
        managed = True
        db_table = 'Student'

    def __str__(self):
        return "Student:%s\tName:%s\tGender:%s" % (self.sno, self.name, self.gender)
