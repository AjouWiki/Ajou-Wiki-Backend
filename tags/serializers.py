from rest_framework.serializers import ModelSerializer
from .models import Tag
from rest_framework import serializers

class TagSerializers(ModelSerializer):

    class Meta:
        model = Tag
        fields = ('name')