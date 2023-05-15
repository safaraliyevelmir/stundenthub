from rest_framework import serializers
from .models import University, Specialty, Tag


class UniversitySerializers(serializers.ModelSerializer):

    class Meta:
        model = University
        fields = '__all__'


class SpecialtySerializers(serializers.ModelSerializer):

    class Meta:
        model = Specialty
        fields = ('title','university')


class TagSerializers(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('title',)
