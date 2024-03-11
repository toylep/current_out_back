from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from base.old_db.models import Faculty
from base.old_db.serializers import CompanySerializer, FacultySerializer, SpecialitySerializer, ThemeSerializer
from base.models import Practice, Companies, Speciality
from base.serializers import PracticeAddSerializer, PracticeListSerializer
from django_filters import rest_framework as filters


class FacultyList(ListAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class ThemeCreateView(CreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = ThemeSerializer


class SpecilityCreateView(CreateAPIView):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer


class PracticeCreateView(CreateAPIView):
    queryset = Practice.objects.all()
    serializer_class = PracticeAddSerializer


class PracticesList(ListAPIView):
    queryset = Practice.objects.all()
    serializer_class = PracticeListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("faculty",)


class CompanyListView(ListAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompanySerializer


class CompanyCreateView(CreateAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompanySerializer


class CompanySingleView(RetrieveUpdateDestroyAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompanySerializer


class FacultyCreateView(CreateAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class FacultySingleView(RetrieveUpdateDestroyAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
