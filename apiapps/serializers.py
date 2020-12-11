from rest_framework import serializers
from apiapps.models import Qualification,Work,Type
from rest_framework.fields import ReadOnlyField


  


class QualificationSerializer(serializers.ModelSerializer):
    qt=ReadOnlyField(source="qualification")
    desc=ReadOnlyField(source="description")
    class Meta:
        model=Qualification
        fields=['qt','desc']

class WorkSerializer(serializers.ModelSerializer):
    wp=ReadOnlyField(source="workprofile")
    desc=ReadOnlyField(source="description")

    class Meta:
        model=Work
        fields=['wp','desc']



class TypeSerializer(serializers.ModelSerializer):
    gt=ReadOnlyField(source="key")
    desc=ReadOnlyField(source="description")
    class Meta:
        model=Type
        fields=['gt','desc']



    