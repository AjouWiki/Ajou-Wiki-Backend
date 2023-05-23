from django.db import models


# Create your models here.
class Tag(models.Model):
    id = models.AutoField(
        primary_key=True,

    )

    name = models.CharField(
        max_length=30,
        null=False,
    )

    wiki_id = models.ForeignKey(
        "wikis.Wiki",
        related_name="tag",
        on_delete=models.CASCADE,
        null=True,
    )
