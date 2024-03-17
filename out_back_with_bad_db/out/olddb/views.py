from django.shortcuts import render

# Create your views here.
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
# from models import Faculty
from olddb.serializers import CompanySerializer, FacultySerializer, SpecialitySerializer, ThemeSerializer
from olddb.models import Faculty
from django_filters import rest_framework as filters


class FacultyList(ListAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class FacultyCreateView(CreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class FacultySingleView(RetrieveUpdateDestroyAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
