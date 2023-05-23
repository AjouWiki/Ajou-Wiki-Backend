from rest_framework.serializers import ModelSerializer
from .models import Tag

from wikis.serializers import WikiSerializer
class TagSerializers(ModelSerializer):
    wiki_id = WikiSerializer(many=True, read_only=True)
    class Meta:
        model = Tag
        fields = (
            "id",
            "name",
            "wiki_id",
        )