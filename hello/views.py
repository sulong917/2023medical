from django.http import HttpResponse


def hello_world(request):
    """显示学生信息的视图"""
    return HttpResponse("<h1>20231201045 何芝锳</h1>")


def hello_name(request, name):
    """带参数的视图"""
    return HttpResponse(f"<h1>20231201045 何芝锳</h1><p>你好，{name}！</p>")