from django.db import models

# Create your models here.

class tags(models.Model):

    id = models.IntegerField(
        primary_key=True,
        unique=True,
    )
        
    

    wiki_id = models.ForeignKey(
        "wiki.Wiki",
        on_delete=models.CASCADE,
        related_name="tags",
        null=True,
    )


    name = models.CharField(
        max_length=30,
        default="",
    )