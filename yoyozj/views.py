from django.shortcuts import render, HttpResponse
from yoyozj.models import Article, ArticleManager

# Create your views here.

def index(request):
    context = {
        'active_menu': 'homepage'
    }
    return render(request, 'yoyozj/index.html', context)
    # return HttpResponse('欢迎来到悠悠然网站')

def fresh_food(request):

    fresh_food_list = Article.objects.all()

    print(fresh_food_list)
    # print(ArticleManager.query_by_column())

    context = {
        'fresh_food_list': fresh_food_list,
        'active_menu': 'freshfood',
    }
    return render(request, 'yoyozj/freshfood.html', context)