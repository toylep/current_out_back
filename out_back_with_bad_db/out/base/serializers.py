from rest_framework.serializers import ModelSerializer
from base.models import DocLink, Practice, Speciality, Theme
from olddb.serializers import CompanySerializer
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "is_staff",
            "is_superuser",
        ]
        read_only_fields = ('id',"is_superuser")
        extra_kwargs = {
            'password': {'write_only': True}
        }

class AuthSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "password",
        ]
        write_only_fields = ("password",)  

class DockLinkSerializer(ModelSerializer):
    class Meta:
        model = DocLink
        fields = "__all__"


class PracticeAddSerializer(ModelSerializer):
    class Meta:
        model = Practice
        fields = "__all__"


class SpecialitySerializer(ModelSerializer):

    class Meta:
        model = Speciality
        fields = "__all__"
    
class ThemeSerializer(ModelSerializer):

    class Meta:
        model = Theme
        fields = '__all__'
        write_only_fields = ('company',)

class PracticeListSerializer(ModelSerializer):
    company = CompanySerializer()
    doc_links = DockLinkSerializer(many=True)
    themes = ThemeSerializer(many=True)
    class Meta:
        model = Practice
        fields = "__all__"