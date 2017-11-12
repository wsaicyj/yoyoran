from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    context = {
        'active_menu': 'homepage'
    }
    return render(request, 'yoyozj/index.html', context)
    # return HttpResponse('欢迎来到悠悠然网站')

def freshfood(request):
    context = {
        'active_menu': 'freshfood'
    }
    return render(request, 'yoyozj/freshfood.html', context)