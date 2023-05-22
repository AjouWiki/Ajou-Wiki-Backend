from rest_framework.serializers import ModelSerializer
from .models import Wiki_Detail
from rest_framework import serializers


class WikiDetailSerializer(ModelSerializer):
    class Meta:
        model = Wiki_Detail
        fields = "__all__"
