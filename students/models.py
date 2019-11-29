
from django.db import models
from  django.contrib.auth.models import User

gender= [('male', 'Male'), ('female', 'Female'), ('other', 'Other')]
semester = [('first','First'),('second','Second'),('third','Third'),('fourth','Fourth'),('fifth','Fifth'),('sixth','Sixth'),('seventh','Seventh'),('eight','Eight')]
year = [('first','First'),('second','Second'),('third','Third'),('fourth','Fourth')]
faculty= [('bca', 'BCA'), ('csit','CSIT')]

class Students(models.Model):
    fullname= models.CharField(max_length=30)
    contact_no= models.CharField(max_length=15)
    address= models.CharField(max_length=50, null=True, blank= True)
    profile= models.ImageField(upload_to='profile/', null= True, blank=True)
    semester = models.CharField(max_length=7, choices=semester)
    year = models.CharField(max_length=7, choices=year)
    gender= models.CharField(max_length=6, choices=gender)
    faculty= models.CharField(max_length=5, choices=faculty)
    about=models.TextField(null= True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return  self.fullname
