from base.serializers import DockLinkSerializer
from base.serializers import (
    PracticeAddSerializer,
    PracticeListSerializer,
    ThemeSerializer,
    SpecialitySerializer,
)

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from base.models import Practice, DocLink, Speciality, Theme
from django_filters import rest_framework as filters

# Create your views here.


class SpecilityCreateView(CreateAPIView):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer

class SpecialityList(ListAPIView):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer

class SpecialitySingleView(RetrieveUpdateDestroyAPIView):
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

class PracticeSingleView(RetrieveUpdateDestroyAPIView):
    queryset = Practice.objects.all()
    serializer_class = PracticeListSerializer


class DocLinkCreateView(CreateAPIView):
    queryset = DocLink.objects.all()
    serializer_class = DockLinkSerializer


class ThemeCreateView(CreateAPIView):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer
