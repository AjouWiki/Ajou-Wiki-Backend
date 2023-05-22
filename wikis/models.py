from django.db import models
from common.models import CommonModel


# Create your models here.
class Wiki(CommonModel):

    """Wiki Model Definition"""

    name = models.CharField(
        max_length=30,
        default="",
    )

    user_id = models.ForeignKey(
        "users.User",
        related_name="wikis",
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self) -> str:
        return self.name
