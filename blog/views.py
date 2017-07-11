from django.shortcuts import render
from blog.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms.models import model_to_dict

# Create your views here.
def index(request):
    article = Article.objects.filter(istop=True)
    page = request.GET.get('page')
    paginator = Paginator(article, 6)  # Show 5 contacts per page
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    tag = Tag.objects.all()
    category = Category.objects.all()
    return  render(request, "index.html", locals())

def articles(request, param):
    tag = Tag.objects.all()
    category = Category.objects.all()
    try:
        if param == '':
            page = request.GET.get('page')
            paginator = Paginator(Article.objects.all(), 10)  # Show 5 contacts per page
            try:
                contacts = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                contacts = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                contacts = paginator.page(paginator.num_pages)
        else:
            article = Article.objects.get(id=int(param))
            first_comment = Comment.objects.filter(article = int(param), pid = None)
            rear_comment = Comment.objects.filter(article=int(param), pid_id__isnull=True)
            comment = {}
            # for cmt in rear_comment:
                # if cmt.pid == None:
                #     comment.append({'id':cmt.id, 'content':cmt.content, 'username':cmt.username, 'date_publish':cmt.date_publish, 'pid': cmt.pid})
                # else:
            #     comment.append(model_to_dict(cmt))
            # print(comment)
        return render(request, "article.html", locals())
    except :
        return render(request, "404.html", {"error" : "提交链接非法."})

def category(request, param):
    tag = Tag.objects.all()
    category = Category.objects.all()
    try:
        if param == '':
            article = Article.objects.filter(category=1)
            category_name = Category.objects.get(id=1)
        else:
            article = Article.objects.filter(category=int(param))
            category_name = Category.objects.get(id=int(param))
        page = request.GET.get('page')
        paginator = Paginator(article, 6)  # Show 5 contacts per page\
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)
        return render(request, "category.html", locals())
    except:
        return render(request, "404.html", {"error": "提交链接非法."})

def tag(request, param):
    tag = Tag.objects.all()
    category = Category.objects.all()
    try:
        if param == '':
            article = Article.objects.filter(tag=1)
            tag_name = Tag.objects.get(id=1)
        else:
            article = Article.objects.filter(tag=int(param))
            tag_name = Tag.objects.get(id=int(param))
        page = request.GET.get('page')
        paginator = Paginator(article, 6)  # Show 5 contacts per page\
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = paginator.page(paginator.num_pages)
        return render(request, "tag.html", locals())
    except:
        return render(request, "404.html", {"error": "提交链接非法."})

def about(request):
    return render(request, "about.html",)