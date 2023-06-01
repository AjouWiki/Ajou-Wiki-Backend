from rest_framework.serializers import ModelSerializer
from .models import Wiki_Detail
from rest_framework import serializers
# from users.serializers import UserSerializer

# from users.serializers import UserSerializer


class WikiDetailsSerializer(ModelSerializer):
    class Meta:
        model = Wiki_Detail
        fields = "__all__"


class MakeWikiDetailsSerializer(ModelSerializer):
    # user_id = UserSerializer(read_only=True)

    class Meta:
        model = Wiki_Detail
        fields = (
            "title",
            "order",
            "description",
            "wiki_id",
            "user_id",
        )
