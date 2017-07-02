# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.

# 分类模型
class Category(models.Model):
    name = models.CharField('类名', max_length=20)
    rank = models.IntegerField('序号', unique=True)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 标签模型
class Tag(models.Model):
    name = models.CharField('标签名', max_length=20)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

# 文章模型
class Article(models.Model):
    title = models.CharField('标题', max_length=60)
    describe = models.TextField('描述', max_length=500)
    content = models.TextField('正文')
    create_date = models.DateTimeField('创建时间', auto_now_add=True)
    page_view = models.IntegerField('浏览量', default=0)
    support = models.IntegerField('赞', default=0)
    trample = models.IntegerField('踩', default=0)
    istop = models.BooleanField('是否置顶', default=False)
    category = models.ForeignKey(Category, verbose_name = '分类')
    tag = models.ManyToManyField(Tag, verbose_name='标签')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.title)

# 评论模型
class Comment(models.Model):
    content = models.TextField(verbose_name='评论内容')
    username = models.CharField(verbose_name='用户名', max_length=30, blank=True, null=True)
    email = models.EmailField(verbose_name='邮箱地址', max_length=50, blank=True, null=True)
    date_publish = models.DateTimeField('发布时间', auto_now_add=True)
    # user = models.ForeignKey(User, verbose_name='用户', blank=True, null=True)
    # url = models.URLField(verbose_name='个人地址', max_length=100, blank=True, null=True)
    article = models.ForeignKey(Article, verbose_name='文章')
    pid = models.ForeignKey('self', verbose_name='父级评论', blank=True, null=True)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content

# 用户模型
# class User(models.Model):
#     pass