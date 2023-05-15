from django.shortcuts import render
from rest_framework import viewsets
from .models import University, Specialty, Tag
from .serializers import UniversitySerializers, SpecialtySerializers, TagSerializers

class UniversityViewSet(viewsets.ModelViewSet):

    queryset = University.objects.all()
    serializer_class = UniversitySerializers


class SpecialtyViewSet(viewsets.ModelViewSet):

    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializers



class TagViewSet(viewsets.ModelViewSet):

    queryset = Tag.objects.all()
    serializer_class = TagSerializers