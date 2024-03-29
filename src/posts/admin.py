from django.contrib import admin
from ckeditor_uploader.fields import RichTextUploadingField
from .models import Author, Category, Post, Comment, PostView

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostView)


class ModelClass:
    content = RichTextUploadingField()
