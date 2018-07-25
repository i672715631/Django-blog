from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Article, BlogType
from django.core.paginator import Paginator
from django.conf import settings

# Create your views here.
def article_detail(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        context = {
            'article_obj': article,
        }  # 这里跟教程不一样，这是新的改动
        # return render(request, "article_detail.html", context)
        return render_to_response("article_detail.html", context)
    except Article.DoesNotExist:
        raise Http404("页面不存在")
    # return HttpResponse('<h2>文章标题id: %s </h2> <br> <p> 文章内容：%s </p>' % (article.title,article.content))


# 使用simple_article_detail中
def simple_article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {
        'article_obj': article,
    }
    return render_to_response("article_detail.html", context)


def article_list(request):
    # articles = Article.objects.filter(is_deleted=False)
    article_all_list = Article.objects.all()
    paginator = Paginator(article_all_list, settings.EACH_PAGE_BLOG_NUM)
    page_num = request.GET.get('page', 1)  # 获取url页面参数（GET请求）
    page_of_articles = paginator.get_page(page_num)
    context = {
        'articles': page_of_articles.object_list,
        'page_of_articles': page_of_articles,
        'articles_count': Article.objects.all().count(),
        'blog_types': BlogType.objects.all(),
    }
    return render_to_response("article_list.html", context)


def blog_with_type(request, blog_type_pk):
    context = {}
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    article_all_list = Article.objects.filter(blog_type=blog_type)
    paginator = Paginator(article_all_list, settings.EACH_PAGE_BLOG_NUM)
    page_num = request.GET.get('page', 1)  # 获取url页面参数（GET请求）
    page_of_articles = paginator.get_page(page_num)
    context['blog_type'] = blog_type
    context['blog_types'] = BlogType.objects.all()
    context['page_of_articles'] = page_of_articles
    context['articles'] = page_of_articles.object_list
    return render_to_response('blog_with_type.html', context)