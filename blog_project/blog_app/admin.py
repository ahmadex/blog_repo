from django.contrib import admin
from blog_app.models import Blog
# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
  list_display = ['id', 'title', 'body', 'author', 'created', 'publish_date']