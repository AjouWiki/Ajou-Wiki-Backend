from django.db import models
from common.models import CommonModel


# Create your models here.
class Wiki(CommonModel):

    """Wiki Model Definition"""

    name = models.CharField(
        max_length=30,
        default="",
    )

    wiki_detail = models.ManyToManyField(
        "wiki_detail.Wiki_Detail",
        related_name="wiki",
        blank=True,
    )

    user_id = models.ForeignKey(
        "users.User",
        related_name="wiki",
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self) -> str:
        return self.name
