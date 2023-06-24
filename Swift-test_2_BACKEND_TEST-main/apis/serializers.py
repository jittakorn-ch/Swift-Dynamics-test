from rest_framework import serializers
from .models import *


class SchoolStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolStructure
        fields = '__all__'


class SchoolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schools
        fields = '__all__'


class ClassesSerializer(serializers.ModelSerializer):
    school = SchoolsSerializer()

    class Meta:
        model = Classes
        fields = '__all__'


class PersonnelSerializer(serializers.ModelSerializer):
    school_class = ClassesSerializer()

    class Meta:
        model = Personnel
        fields = '__all__'


class SubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = '__all__'


class StudentSubjectsScoreSerializer(serializers.ModelSerializer):
    student = PersonnelSerializer()
    subjects = SubjectsSerializer()

    class Meta:
        model = StudentSubjectsScore
        fields = '__all__'
