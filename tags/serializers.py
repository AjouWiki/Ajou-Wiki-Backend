from rest_framework.serializers import ModelSerializer
from .models import Tag
from wiki.models import Wiki
from wiki.serializers import WikiSerializer
from rest_framework import serializers

class TagSerializers(ModelSerializer):

    class Meta:
        model = Tag
        fields = ('name')