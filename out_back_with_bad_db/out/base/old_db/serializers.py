from rest_framework.serializers import ModelSerializer, StringRelatedField
from base.old_db.models import Companies, Faculty
from base.models import Speciality, Theme


class CompanySerializer(ModelSerializer):
    themes = StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Companies
        fields = "__all__"


class SpecialitySerializer(ModelSerializer):

    class Meta:
        model = Speciality
        fields = "__all__"


class FacultySerializer(ModelSerializer):

    specialities = StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Faculty
        fields = "__all__"


class ThemeSerializer(ModelSerializer):

    class Meta:
        model = Theme
        fields = '__all__'
        write_only_fields = ('company',)
