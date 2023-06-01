from rest_framework.serializers import ModelSerializer
from .models import Tag

from wikis.serializers import WikiSerializer
from drf_yasg import openapi

class TagSerializers(ModelSerializer):
    wiki_id = None
    name = openapi.Schema(
        type=openapi.TYPE_STRING,
        title='태그 이름',
        max_length=30,
        min_length=1,
    )

    class Meta:
        model = Tag

        fields = (
            "id",
            "name",
        )
        