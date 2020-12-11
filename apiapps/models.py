from django.db import models


# Create your models here.
class Qualification(models.Model):
    qualification=models.CharField(max_length=50,null=False)
    description=models.CharField(max_length=50,null=True)
    isactive=models.BooleanField(null=False,default=0)

    class Meta:
        constraints=[models.UniqueConstraint(
            fields=['qualification'],name='guardian_qualification_uk_qualification'
        )]
        
        




class Work(models.Model):
    workprofile=models.CharField(max_length=500)
    description=models.CharField(max_length=500)
    isactive=models.BooleanField(null=False,default=1)


    class Meta:
        constraints=[models.UniqueConstraint(
            fields=['workprofile'],name='guardian_work_uk_workprofile'
        )]



class Type(models.Model):
    key=models.CharField(max_length=500,primary_key=True)
    description=models.CharField(max_length=500)
    isactive=models.BooleanField(null=False,default=1)






    





