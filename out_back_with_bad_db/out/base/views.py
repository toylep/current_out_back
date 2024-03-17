from django.shortcuts import render
from base.serializers import DockLinkSerializer
from base.models import Practice, Companies, Speciality, DocLink, Theme
from base.serializers import PracticeAddSerializer, PracticeListSerializer
from olddb.serializers import (
    CompanySerializer,
    FacultySerializer,
    SpecialitySerializer,
    ThemeSerializer,
)
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from django_filters import rest_framework as filters

# Create your views here.


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


class DocLinkCreateView(CreateAPIView):
    queryset = DocLink.objects.all()
    serializer_class = DockLinkSerializer


class ThemeCreateView(CreateAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
