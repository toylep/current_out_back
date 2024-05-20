# Create your views here.
from django_filters import rest_framework as filters
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAdminUser

from olddb.models import Faculty, Companies
# from models import Faculty
from olddb.serializers import CompanySerializer, FacultySerializer


class FacultyList(ListAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class FacultyCreateView(CreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class FacultySingleView(RetrieveUpdateDestroyAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class CompanyListView(ListAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompanySerializer


class CompanyFullListView(ListAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompanyFullSerializer


class CompanyCreateView(CreateAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAdminUser]


class CompanySingleView(RetrieveUpdateDestroyAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompanySerializer
