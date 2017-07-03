from django.shortcuts import render
from blog.models import *

# Create your views here.
def index(request):
    article = Article.objects.all()
    tag = Tag.objects.all()
    category = Category.objects.all()
    return  render(request, "index.html", locals())

def articles(request, param):
    article = Article.objects.get(id=int(param))
    tag = Tag.objects.all()
    category = Category.objects.all()
    return  render(request, "article.html", locals())