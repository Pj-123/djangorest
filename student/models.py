from django.db import models


# Create your models here.


# Create your models here.
class Student(models.Model):
    user_name=models.CharField(max_length=50,null=True)
    first_name=models.CharField(max_length=20)
    middle_name=models.CharField(max_length=20,null=True)
    last_name=models.CharField(max_length=20)
    reg_number=models.CharField(max_length=20)
    roll_number=models.CharField(max_length=10)
    mobile=models.CharField(max_length=15,null=True)
    email=models.CharField(max_length=20,null=True)
    gender=models.CharField(max_length=10,null=True)
    password=models.CharField(max_length=255,null=True)
    isactive=models.BooleanField(null=True,default=1)
    created_at=models.DateTimeField(null=True)
    created_by=models.CharField(max_length=20,null=True)
    updated_at=models.DateTimeField(null=True)
    updated_by=models.CharField(max_length=20,null=True)
    class Meta:
        constraints=[
            models.UniqueConstraint(fields=['user_name'],name='student_uk_user_name'),
            models.UniqueConstraint(fields=['mobile'],name='student_uk_mobile'),
            models.UniqueConstraint(fields=['email'],name='student_uk_email'),
            models.UniqueConstraint(fields=['reg_number'],name='student_uk_reg_no'),
        ]
class AddressType(models.Model):
    addresstype=models.CharField(max_length=50,null=True)
    description=models.CharField(max_length=50,null=True)
    isactive=models.BooleanField(null=True,default=1)
    created_at=models.DateTimeField(null=True)
    created_by=models.CharField(max_length=20,null=True)
    updated_at=models.DateTimeField(null=True)
    updated_by=models.CharField(max_length=20,null=True)
    


class Address(models.Model):
    student_id=models.IntegerField(max_length=50)
    add_type_id=models.IntegerField(max_length=20)
    address=models.CharField(max_length=20)
    house_no=models.CharField(max_length=20)
    locality=models.CharField(max_length=20)
    landmark=models.CharField(max_length=10,null=True)
    city=models.CharField(max_length=15)
    state=models.CharField(max_length=20)
    country=models.CharField(max_length=10)
    pincode=models.CharField(max_length=255)
    priority=models.IntegerField(null=True,default=1)
    isactive=models.BooleanField(null=False,default=1)
    created_at=models.DateTimeField()
    created_by=models.CharField(max_length=20)
    updated_at=models.DateTimeField()
    updated_by=models.CharField(max_length=20)




    




        
        
    
        
 
