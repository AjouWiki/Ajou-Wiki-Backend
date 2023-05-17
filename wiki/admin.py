from django.contrib import admin
from .models import Wiki

# Register your models here.


@admin.register(Wiki)
class WikiAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "get_wiki_detail",
    )

    # list_filter = ("category",)
    def get_wiki_detail(self, obj):
        return "\n".join([p.wiki_detail for p in obj.wiki_detail.all()])
