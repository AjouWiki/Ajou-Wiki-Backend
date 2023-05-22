from django.contrib import admin
from .models import Wiki

# Register your models here.


@admin.register(Wiki)
class WikisAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "get_wiki_details",
        "created_at",
        "updated_at",
        "user_id",
    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related("wiki_details")  # 역참조 필드 미리 가져오기
        return queryset

    def get_wiki_details(self, obj):
        wiki_details = [wiki_detail.title for wiki_detail in obj.wiki_details.all()]
        return ", ".join(wiki_details)

    get_wiki_details.short_description = "Wiki Details"
