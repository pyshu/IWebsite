from django.shortcuts import render
from blog.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.forms import CommentForm

# Create your views here.
def index(request):
    tag = Tag.objects.all()
    category = Category.objects.all()
    newest_article = Article.objects.filter().order_by('-create_date')[:5]
    istop_article = Article.objects.filter(istop=True)
    page = request.GET.get('page')
    paginator = Paginator(istop_article, 6)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return  render(request, "index.html", locals())

def articles(request, param):
    tag = Tag.objects.all()
    category = Category.objects.all()
    newest_article = Article.objects.filter().order_by('-create_date')[:5]
    if request.method == "POST":
        form = CommentForm(request.POST)
        # 判断form是否有效
        print(request.POST)
        if form.is_valid():
            if request.POST['pid'] == "None":
                pid = None
            else:
                pid = int(request.POST['pid'])
            instance = Comment.objects.create(username=request.POST['username'],email=request.POST['email'],content=request.POST['content'],
                                              article_id = int(request.POST['article']),pid_id = pid ,reply_who = request.POST['reply_who'])
            instance.save()
    try:
        if param == '':
            page = request.GET.get('page')
            paginator = Paginator(Article.objects.all(), 10)
            try:
                contacts = paginator.page(page)
            except PageNotAnInteger:
                contacts = paginator.page(1)
            except EmptyPage:
                contacts = paginator.page(paginator.num_pages)
        else:
            article = Article.objects.get(id=int(param))
            article_tag_name = ''
            for t in article.tag.all():
                article_tag_name = article_tag_name+ t.name + ','
            article.page_view = article.page_view + 1
            article.save()
            sql_comment = Comment.objects.filter(article = int(param))
            list_comment = []
            for q_cmt in sql_comment:
                for l_cmt in list_comment:
                    if not hasattr(l_cmt, 'children'):
                        setattr(l_cmt, 'children', [])
                    if q_cmt.pid == l_cmt:
                        l_cmt.children.append(q_cmt)
                if q_cmt.pid == None:
                    list_comment.append(q_cmt)
            form = CommentForm()
        return render(request, "article.html", locals())
    except:
        return render(request, "404.html", {"error" : "提交链接非法."})

def category(request, param):
    tag = Tag.objects.all()
    category = Category.objects.all()
    newest_article = Article.objects.filter().order_by('-create_date')[:5]
    try:
        if param == '':
            article = Article.objects.filter(category=1)
            category_name = Category.objects.get(id=1)
        else:
            article = Article.objects.filter(category=int(param))
            category_name = Category.objects.get(id=int(param))
        page = request.GET.get('page')
        paginator = Paginator(article, 6)
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
        return render(request, "category.html", locals())
    except:
        return render(request, "404.html", {"error": "提交链接非法."})

def tag(request, param):
    tag = Tag.objects.all()
    category = Category.objects.all()
    newest_article = Article.objects.filter().order_by('-create_date')[:5]
    try:
        if param == '':
            article = Article.objects.filter(tag=1)
            tag_name = Tag.objects.get(id=1)
        else:
            article = Article.objects.filter(tag=int(param))
            tag_name = Tag.objects.get(id=int(param))
        page = request.GET.get('page')
        paginator = Paginator(article, 6)
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
        return render(request, "tag.html", locals())
    except:
        return render(request, "404.html", {"error": "提交链接非法."})

def about(request):
    return render(request, "about.html",)