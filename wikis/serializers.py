from rest_framework.serializers import ModelSerializer
from .models import Wiki

# from wiki.models import Wiki
from rest_framework import serializers
from wiki_details.serializers import WikiDetailSerializer


class WikiSerializer(ModelSerializer):
    wiki_details = WikiDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Wiki
        fields = (
            "id",
            "name",
            "wiki_details",
        )
