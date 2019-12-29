from django.contrib import admin
from .models import Post, Announcement, PageDetail, Website

admin.site.register(Post)
admin.site.register(Announcement)
admin.site.register(PageDetail)
admin.site.register(Website)