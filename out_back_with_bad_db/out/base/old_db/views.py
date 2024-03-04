from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from base.old_db.models import Faculty
from base.old_db.serializers import FacultySerializer
from base.models import Practice
from base.serializers import PracticeSerializer
from django_filters import rest_framework as filters


class FacultyList(ListAPIView):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class PracticesList(ListAPIView):
    queryset = Practice.objects.all()
    serializer_class = PracticeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("faculty",)