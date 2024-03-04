from rest_framework.serializers import ModelSerializer, StringRelatedField
from base.old_db.models import Companies, Faculty
from base.models import Speciality


class CompanySerializer(ModelSerializer):

    class Meta:
        model = Companies
        fields = "__all__"


class SpecialitySerializer(ModelSerializer):

    class Meta:
        model = Speciality
        fields = ["name"]


class FacultySerializer(ModelSerializer):

    specialities = SpecialitySerializer(many=True)

    class Meta:
        model = Faculty
        fields = "__all__"
