from django.contrib import admin
from blog.models import *

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(ArticleToTag)
admin.site.register(Comment)