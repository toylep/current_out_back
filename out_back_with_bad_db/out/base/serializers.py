from rest_framework.serializers import ModelSerializer
from base.old_db.models import Companies
from base.models import Practice
from base.old_db.serializers import CompanySerializer


class PracticeSerializer(ModelSerializer):
    company = CompanySerializer()
    
    class Meta:
        model = Practice
        fields = "__all__"