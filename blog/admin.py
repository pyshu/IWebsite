# -*- coding:utf-8 -*-
from django.contrib import admin
from blog.models import *

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title', 'page_view')

    fieldsets = (
        (None, {
            'fields': ('title', 'describe', 'content', 'category','tag')
        }),
        ('高级选项', {
            'classes': ('collapse',),
            'fields': ('page_view', 'support', 'trample', 'istop'),
        }),
    )

    class Media:
        # 在管理后台的HTML文件中加入js文件
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-all.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)