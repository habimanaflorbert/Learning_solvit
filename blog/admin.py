from django.contrib import admin
from blog.models import News,Author,Book, Genre
from django.contrib import messages

# Register your models here.



admin.site.site_header = "MOMO Admin Panel"       # Top left header
admin.site.site_title = "MOMO"                # Browser tab title
admin.site.index_title = "MOMO"  # Index page title

@admin.action(description='Mark selected news as unpublished')
def unpublish(modeladmin, request, queryset):
    updated = queryset.update(is_published=False)
    messages.success(request, f"{updated} news were marked as unpublished.")

@admin.action(description='Mark selected News as Publishing')
def publish(modeladmin, request, queryset):
    updated = queryset.update(is_published=True)
    messages.info(request, f"{updated} news were marked as published.")

class NewsAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','done_at']
    search_fields=['first_name','last_name']
    list_filter=['is_published','done_at']
    actions=[publish,unpublish]


admin.site.register(News,NewsAdmin)






admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
