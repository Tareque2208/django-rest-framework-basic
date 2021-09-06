from django.contrib import admin
from .models import Article, ArticleRating, Course, Tag

# Register your models here.

admin.site.register(Article)
admin.site.register(ArticleRating)
admin.site.register(Tag)
admin.site.register(Course)