from rest_framework.serializers import ModelSerializer
from olddb.models import Companies
from base.models import DocLink, Practice
from olddb.serializers import CompanySerializer


class DockLinkSerializer(ModelSerializer):
    class Meta:
        model = DocLink
        fields = "__all__"


class PracticeAddSerializer(ModelSerializer):
    class Meta:
        model = Practice
        fields = "__all__"


class PracticeListSerializer(ModelSerializer):
    company = CompanySerializer()
    doc_links = DockLinkSerializer(many=True)

    class Meta:
        model = Practice
        fields = "__all__"
