from rest_framework.serializers import ModelSerializer
from .models import Wiki

# from wiki.models import Wiki
from rest_framework import serializers
from wiki_details.serializers import WikiDetailsSerializer
from tags.serializers import TagSerializers


class WikiSerializer(ModelSerializer):
    wiki_details = WikiDetailsSerializer(many=True, read_only=True)
    tags = TagSerializers(many=True, read_only=True)

    class Meta:
        model = Wiki
        fields = (
            "id",
            "name",
            "wiki_details",
            "created_at",
            "updated_at",
            "user_id",
            "tags"
        )


class SmallWikiSerializer(ModelSerializer):
    class Meta:
        model = Wiki
        fields = (
            "id",
            "name",
            "created_at",
            "updated_at",
            "user_id",
        )
