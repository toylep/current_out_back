from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from base.models import DocLink
from base.serializers import DockLinkSerializer
# Create your views here.


class DocLinkCreateView(CreateAPIView):
    queryset = DocLink.objects.all()
    serializer_class = DockLinkSerializer