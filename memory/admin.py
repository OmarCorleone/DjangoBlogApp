from django.contrib import admin
from .models import Memory,Comment
# Register your models here.
@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):

    list_display=["title","author","created_date"]
    list_display_links=["title","author","created_date"]
    search_fields=["title"]
    list_filter=["created_date"]

    class Meta:
        model=Memory

admin.site.register(Comment)

