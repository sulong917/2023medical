from django.shortcuts import render
from django.http import HttpResponse, Http404


def hello_world(request):
    """显示学生信息的视图"""
    return HttpResponse("<h1>20231201045 何芝锳</h1>")


def hello_name(request, name):
    """带参数的视图"""
    return HttpResponse(f"<h1>20231201045 何芝锳</h1><p>你好，{name}！</p>")


def index(request):
    """返回前端页面"""
    return render(request, 'index.html')


def section(request, num):
    """根据传入的整数num返回对应文本"""
    if num < 1 or num > 3:
        raise Http404("Page not found")
    
    texts = {
        1: "This is the content for Page 1",
        2: "This is the content for Page 2", 
        3: "This is the content for Page 3"
    }
    
    return HttpResponse(texts[num])