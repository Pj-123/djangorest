from rest_framework import serializers
from student.models import Student
from rest_framework.fields import ReadOnlyField


  


class QualificationSerializer(serializers.ModelSerializer):
    mob=ReadOnlyField(source="mobile")
    em=ReadOnlyField(source="email")
    class Meta:
        model=Student
        fields=['mob','em']
