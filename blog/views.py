from django.shortcuts import render
from blog.models import *

# Create your views here.
def index(request):
    article = Article.objects.all()
    tag = Tag.objects.all()
    category = Category.objects.all()
    return  render(request, "index_blog.html", locals())