from rest_framework.serializers import ModelSerializer
from .models import User
from wikis.models import Wiki
from wikis.serializers import WikiSerializer, SmallWikiSerializer
from wiki_details.serializers import WikiDetailsSerializer
from rest_framework import serializers


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        exclude = (
            # "password",
            "id",
            "user_permissions",
            "groups",
            "is_staff",
            "is_active",
            "first_name",
            "last_name",
            "is_superuser",
        )

    def validate(self, data):
        check = "@ajou.ac.kr"

        if data["email"][-len(check) :] != check:
            raise serializers.ValidationError("아주대 이메일을 사용하여 주세요.")
        return data


class PrivateUserSerializer(ModelSerializer):
    wikis = SmallWikiSerializer(many=True, read_only=True)  # 역으로 접근한거 related_name
    wiki_details = WikiDetailsSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            "name",
            "department",
            "sex",
            "email",
            "student_id",
            "wikis",
            "wiki_details",
        )
class UserEmailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
        )
class UserNameSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
        )
class UserLoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "password"
        )
