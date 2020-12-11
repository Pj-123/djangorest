from django.contrib import admin
from student.models import *

admin.site.register(Student)
admin.site.register(Address)
admin.site.register(AddressType)

# Register your models here.
