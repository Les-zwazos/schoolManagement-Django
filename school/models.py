from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TeacherExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(null=False)
    joindate=models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=40)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name




classes=[('Class one','Class one'),('Class two','Class two'),('Class three','Class three'),
('Class four','Class four'),('Class five','Class five'),('Class six','Class six'),('Class seven','Class seven'),('Class eight','Class eight'),('Class nine','Class nine'),('Class ten','Class ten')]
class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    roll = models.CharField(max_length=10)
    mobile = models.CharField(max_length=40,null=True)
    fee=models.PositiveIntegerField(null=True)
    cl= models.CharField(max_length=20,choices=classes,default='Class one')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name



class Attendance(models.Model):
    roll=models.CharField(max_length=10,null=True)
    date=models.DateField()
    cl=models.CharField(max_length=10)
    present_status = models.CharField(max_length=10)



class Notice(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=20,null=True,default='school')
    message=models.CharField(max_length=500)



class Course(models.Model):
    title = models.CharField(max_length=200)
    by = models.CharField(max_length=30,null=True,default='The teacher')
    course_class =models.CharField(max_length=20,choices=classes,default='Class one')
    document = models.FileField(upload_to='documents/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title